
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get("https://pythonexamples.org/")
    #find element by id
    myDiv = driver.find_element(By.CLASS_NAME, 'entry-header')
    print(myDiv)
    print(myDiv.text)
    print(myDiv.get_attribute("outerHTML"))