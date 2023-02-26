# https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://www.python.org")    
print(driver.title)