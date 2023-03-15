from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('http://127.0.0.1:5500/localwebsite/index.html')
    # find element by link text
    # <a href="/about/">About this article</a>
    myDiv = driver.find_element(By.LINK_TEXT, 'About this article')
    print(myDiv.get_attribute("outerHTML"))