"""
#   If find_element() function finds more than one element by the 
    given id, then it returns only the first element.
#   If find_element() function finds no element by the given id,
    then it raises NoSuchElementException.    
"""
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get("https://pythonexamples.org/")
    #find element by id
    myDiv = driver.find_element(By.ID, 'xyz')
    print(myDiv)
    print(myDiv.text)
    