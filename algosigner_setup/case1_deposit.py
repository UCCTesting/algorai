from lib2to3.pgen2 import driver
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

def openAlgoVault():
    print("Open Algo Vault")
    driver.implicitly_wait(20)
    driver.find_element(By.CLASS_NAME, 'flex items-center').click()
    ALGO_VAULT = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[3]/div/div[2]/div[2]').getAtrribute("class")
    print(ALGO_VAULT)

    def openAlgoVault():
    print("Open Algo Vault")
    driver.implicitly_wait(20)
    driver.find_elements(By.CLASS_NAME, 'block.h-6.w-6.false')[1].click()
    print("Succses Open Vault")
    ALGO_VAULT = driver.find_elements(By.CLASS_NAME, 'block.h-6.w-6.false')[1].get_attribute("class")
    print(ALGO_VAULT)

    button = driver.find_element(By.XPATH,"//button[contains( text( ), 'Opt In')]").is_displayed()
    assert button is True

    button.click()
openAlgoVault()