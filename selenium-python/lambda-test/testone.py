# https://www.lambdatest.com/blog/getting-started-with-selenium-python/
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep 
import time 

path = ".\chromedriver.exe"
website = "https://lambdatest.github.io/sample-todo-app/"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.maximize_window()
ele_one = driver.find_element("name","li1") 
ele_two = driver.find_element("name", "li2")
ele_one.click()
ele_two.click()
time.sleep(2)
driver.quit()