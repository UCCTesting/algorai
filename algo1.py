from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions

chrome_options = ChromeOptions()
chrome_options.add_extension(r'C:\\Users\\user\\Documents\\VSCode_Python\\.selenium_python\\algosigner.crx')
driver = webdriver.Chrome(r'C:\\Users\\user\\Documents\\VSCode_Python\\.selenium_python\\chromedriver.exe', options=chrome_options)
driver.maximize_window()
driver.get('http://app-algorai.devucc.name')

input('Press [ENTER] to close browser...')

driver.quit()