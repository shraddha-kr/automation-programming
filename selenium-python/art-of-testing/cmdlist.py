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
# driver.get(website)
# print("Done.... 1")

driver.get("https://www.google.com/")
print("Done.... 2")

# writing to a textbox
el = driver.find_element("name", "q")
el.send_keys("ÄrtOftesting")

# fetch the text written over the web element
text = el.text
print(text)

# clearing text in a textbox
el.clear()

# back button in web browser
driver.back()

# forward button in web browser
driver.forward()

# refresh button in web browser
driver.refresh()
driver.quit()