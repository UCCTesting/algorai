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

WEB_SESSION = os.getcwd() + '\\web-session'

driverPath = os.getcwd() + '\\chromedriver.exe'

password = 'Abc12345'

confirmPassword = 'Abc12345'

accountName = 'Algorai-1'

recoveryPhrase = 'drastic saddle useful typical hawk reward slab true fiscal inch false define humble catalog october repair word soul bounce coyote drip trap flush absorb grant'

def launchWebDriver(driverPath):
    chrome_options = Options()
    chrome_options.add_argument('--profile-directory-Default')
    # directory to store the web session
    # the directory must exist
    chrome_options.add_argument(WEB_SESSION)
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
    driver.maximize_window()
    print('Success Launch Web Driver')
    return driver

launchWebDriver(driverPath)

def setupMyAlgo():
    print("Setup MyAlgo")
    driver.implicitly_wait(10)

    # load my algo html page
    driver.get('https://wallet.myalgo.com/bridge/connect')
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div[2]/a').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div/div/div/div[4]/label/input').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div/div/div/div[5]').click()

    # input password
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys(confirmPassword)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div/div/div[2]/form/button').click()

    # switch network to testNet
    print("opening network dropdown")
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div/div[2]').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div/div[2]').click()
    print("TestNet selected")

    # import account
    print("Import Account")
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[1]/div[2]/div[1]/div[3]/div').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[1]/div[2]/div[1]/div/input').send_keys(accountName)
    driver.find_element(By.XPATH, '//*[@id="0"]').send_keys(recoveryPhrase)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/div[2]/input').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/button').click()

    try:        
        time.sleep(10)
        status=driver.find_element(By.XPATH, '//*[@id="address-copy-tooltip"]/div[2]/div[1]').is_displayed()
        print("Success Import Account")
        assert status is True
    except TimeoutException:
        print("Import Failed")
        pass

    return driver

setupMyAlgo()

def connectToWebsite():
    driver.implicitly_wait(10)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    # open algorai website
    driver.get('app.wagmiswap.io')

    # connect wallet - algosigner
    driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="connect-wallet"]/div[2]/div[4]]').click() 
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div/button[2]').click()

    try:        
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        status=driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div[1]/div/button').is_displayed()
        print("Success Connect My Algo")
        assert status is True
    except TimeoutException:
        print("Connect Wallet Failed")
        pass

    return driver

connectToWebsite()





