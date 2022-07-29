import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

EXTENSION_PATH = os.getcwd() + '\\algosigner_setup\\algosigner.crx'

EXTENSION_ID = 'kmmolakhbgdlpkjkcjkebenjheonagdm'

WEB_SESSION = os.getcwd() + '\\algosigner_setup\\web-session'

DRIVER_PATH = os.getcwd() + '\\algosigner_setup\\driver\\chromedriver.exe'

# read from account_info.txt which returns our account name and password
def account_info():
    with open('algosigner_setup\\account_info.txt', 'r') as f:
        info = f.read().split()
        accountName = info[0]
        password = info[1]
    return accountName, password

# storing email and password
accountName, password = account_info()

# read from recovery_phrase.txt which returns our account address mnemonic
def recovery_phrase():
    with open('algosigner_setup\\recovery_phrase.txt', 'r') as f:
        recoveryPhrase = f.read()
    return recoveryPhrase

# storing email and password
recoveryPhrase = recovery_phrase()

def installExtension():
    print('path', EXTENSION_PATH)

    # use global variable for options
    global chrome_options
    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    chrome_options.add_argument('--profile-directory-Default')
    # directory to store the web session
    # the directory must exist
    chrome_options.add_argument(WEB_SESSION)
    print("Extension has been loaded")

# call function
installExtension()

# creating an instane of our webdriver and applying options
def launchSeleniumWebDriver(DRIVER_PATH):
    print("launch selenium web driver")
    
    # use global variable for driver
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=DRIVER_PATH)

    # maximized the windows
    chrome_options.add_argument("start-maximized")
    driver.maximize_window()

    chrome_options.add_argument('--profile-directory-Default')

    # directory to store the web session, the directory must exist
    chrome_options.add_argument(WEB_SESSION) 
    return driver

# call function
launchSeleniumWebDriver(DRIVER_PATH)

def setupAlgosigner():
    print("Setup Algosigner")
    driver.implicitly_wait(20)

    # load algosigner html page
    driver.get('chrome-extension://{}/index.html'.format(EXTENSION_ID))
    driver.find_element(By.ID, 'setPassword').click()

    # create new wallet
    driver.find_element(By.ID, 'setPassword').send_keys(password)
    driver.find_element(By.ID, 'confirmPassword').send_keys(password)
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
        time.sleep(3)
        assert status is True
    except TimeoutException:
        print("Import Failed")
        pass

    return driver

setupAlgosigner()

def connectToWebsite():
    driver.implicitly_wait(20)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    # open algorai website
    driver.get('http://app-algorai.devucc.name')

    # connect wallet - algosigner
    driver.find_element(By.CLASS_NAME, 'WalletConnect_button__34u_q').click()
    driver.find_elements(By.CLASS_NAME, 'WalletDialogDisconnected_button-wallet__gavVQ')[1].click()
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element(By.ID, 'grantAccess').click()

    try:        
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        status=driver.find_element(By.CLASS_NAME, 'WalletConnect_button__34u_q.false').is_displayed()
        print("Success Connect Algosigner")
        assert status is True
    except TimeoutException:
        print("Connect Wallet Failed")
        pass

    return driver

connectToWebsite()





