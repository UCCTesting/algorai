import time
import time
import os
from xml.dom.minidom import Element
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

password = 't4shi@nna'

confirmPassword = 't4shi@nna'

accountName = 'demo2'

recoveryPhrase = 'walk, common, biology, task, surround, gossip, slogan, today, during, bench, scare, choice, renew, goddess, project, tape, chat, swap, talent, sing, perfect, junior, image, absent, marble'

def MyAlgoWallet_init(driverPath):
    chrome_options = Options()
    chrome_options.add_argument('--profile-directory-Default')
    # directory to store the web session
    # the directory must exist
    chrome_options.add_argument(WEB_SESSION)
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
    driver.maximize_window()

MyAlgoWallet_init(driverPath)

def connectToWebsite():
    driver.implicitly_wait(10)
    driver.get('http://app-algorai.devucc.name')

    # connect wallet - myalgowallet
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/header/div[4]/div/div[1]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/header/div[4]/div/div[1]/div/div/div/div[2]/button[3]').click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/div[2]/a').click()
    driver.switch_to.window(driver.window_handles[1])

    #login to my algo wallet
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[2])
    #agree to terms and agreement
    driver.find_element(By.XPATH, '//html/body/div/div[2]/div/div[1]/div/div/div/div/div[4]/label/input').click()
    driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[1]/div/div/div/div/div[5]/button').click()
    #insert password
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div/div[1]/div/div/div/div[2]/form/div/div[1]/div[2]/div/input").send_keys(password)
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/input").send_keys(confirmPassword)
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div/div[1]/div/div/div/div[2]/form/button/div/div").click()
    #select testnet
    driver.find_element(By.CLASS_NAME,"_9w6ztc").click()
    driver.find_element(By.CLASS_NAME,"_1s54rqk").click()
    #import account
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[2]/div[1]").click()
    #insert mnemonic words
    driver.find_element(By.XPATH,"//div[@id='root']/div[2]/div[3]/div[1]/div[2]/div[1]/div/input").send_keys(accountName)
    driver.find_element(By.NAME,'input-24').send_keys(recoveryPhrase)
    driver.find_element(By.CLASS_NAME,"_u02imw").click()
    #reenter password
    driver.find_element(By.CLASS_NAME,"_11oc14n.form-control").send_keys(password)
    driver.find_element(By.CLASS_NAME,"_16vtsuu").click()

    #my algo wallet to algorai
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[1]/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div[2]/div/form/div[2]/button[2]').click()
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div').click()
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[1]/div[3]/div/div/button[2]').click()

    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    
connectToWebsite()