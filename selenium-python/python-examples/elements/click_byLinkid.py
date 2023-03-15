from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="C:/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('http://127.0.0.1:5500/index.html')
    #find element by id
    # <a id="aboutLink" href="/about.html">About Hello World</a>
    myLink = driver.find_element(By.ID, 'aboutLink')
    myLink.click()