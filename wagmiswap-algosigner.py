import time
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import urllib.request

EXTENSION_PATH = os.getcwd() + '\\algosigner.crx'

EXTENSION_ID = 'kmmolakhbgdlpkjkcjkebenjheonagdm'

WEB_SESSION = os.getcwd() + '\\web-session'

driverPath = os.getcwd() + '\\chromedriver.exe'

password = 'Abc12345'

confirmPassword = 'Abc12345'

accountName = 'Algorai-1'

recoveryPhrase = 'drastic saddle useful typical hawk reward slab true fiscal inch false define humble catalog october repair word soul bounce coyote drip trap flush absorb grant'

def launchSeleniumWebdriver(driverPath):
    print('path', EXTENSION_PATH)
    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    chrome_options.add_argument('--profile-directory-Default')
    # directory to store the web session
    # the directory must exist
    chrome_options.add_argument(WEB_SESSION)
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
    driver.maximize_window()
    driver.implicitly_wait(10)
    print("Extension has been loaded")
    return driver

launchSeleniumWebdriver(driverPath)

def setupAlgosigner():
    print("Setup Algosigner")
    driver.implicitly_wait(10)
    driver.get('chrome-extension://{}/index.html'.format(EXTENSION_ID))
    driver.find_element(By.ID, 'setPassword').click()

    # create new wallet
    driver.find_element(By.ID, 'setPassword').send_keys(password)
    driver.find_element(By.ID, 'confirmPassword').send_keys(confirmPassword)
    driver.find_element(By.ID, 'createWallet').click()

    # switch network to testNet
    print("opening network dropdown")
    driver.find_element(By.ID, 'selectLedger').click()
    driver.find_element(By.ID, 'selectTestNet').click()
    print("TestNet selected")

    # add account
    print("Add Account")
    driver.find_element(By.ID, 'addAccount').click()

    # import account
    print("Import Account")
    driver.find_element(By.ID, "importAccount").click()
    driver.find_element(By.ID, 'accountName').send_keys(accountName)
    driver.find_element(By.ID, 'mnemonicWord0').send_keys(recoveryPhrase)
    driver.find_element(By.ID, 'nextStep').click()
    driver.find_element(By.ID, 'enterPassword').send_keys(password)
    driver.find_element(By.ID, 'authButton').click()

    try:        
        time.sleep(10)
        status=driver.find_element(By.ID, 'account_' + accountName).is_displayed()
        print("Success Import Account")
        assert status is True
    except TimeoutException:
        print("Import Failed")
        pass

setupAlgosigner()

def connectToWebsite():
    driver.implicitly_wait(10)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://app.wagmiswap.io/swap')
    driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="connect-wallet"]/div[2]/div[3]').click() 
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element(By.ID, 'grantAccess').click()

connectToWebsite()





