from selenium import webdriver
#from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions

chrome_options = ChromeOptions()
chrome_options.add_extension(r'C:\\Users\\user\\Documents\\VSCode_Python\\selenium_python\\algosigner.crx')
chrome_options.add_argument('--profile-directory-Default')
# directory to store the web session
# the directory must exist
chrome_options.add_argument(r'--user-data-dir=C:\\Users\\user\\Documents\\VSCode_Python\\selenium_python\\websession')
driver = webdriver.Chrome(r'C:\\Users\\user\\Documents\\VSCode_Python\\selenium_python\\chromedriver.exe', options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
#driver.get('http://app-algorai.devucc.name')
algosigner_url = 'chrome-extension://kmmolakhbgdlpkjkcjkebenjheonagdm/index.html#/login/'
driver.get(algosigner_url)
algosigner_window = driver.current_window_handle

password = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.ID, "enterPassword"))
    )
# put in your algosigner password
password.send_keys('Abc12345')

login = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
login.click()

selectLedger = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.ID, "selectLedger"))
    )
selectLedger.click()

selectTestNet = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.ID, "selectTestNet"))
    )
selectTestNet.click()

addAccount = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.ID, "addAccount"))
    )
addAccount.click()

importAccount = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.ID, "importAccount"))
    )
importAccount.click()

input('Press [ENTER] to close browser...')
driver.quit()