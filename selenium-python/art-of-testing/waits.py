# https://artoftesting.com/waits-in-selenium-webdriver
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep 
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
path = ".\chromedriver.exe"
website = "https://artoftesting.com/waits-in-selenium-webdriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
print("Done.")
# implicit wait - https://www.geeksforgeeks.org/implicit-waits-in-selenium-python/
driver.implicitly_wait(5)
driver.maximize_window()

# explicit wait - https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/?ref=rp
try:
    el = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, "myDynamicElement"))
finally:
    driver.quit()