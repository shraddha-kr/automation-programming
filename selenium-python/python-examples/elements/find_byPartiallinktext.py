from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('http://127.0.0.1:5500/localwebsite/index.html')
    # find element by partial link text
    # <a href="/new-article/">About New Article</a>
    myDiv = driver.find_element(By.PARTIAL_LINK_TEXT, 'New Article')
    print(myDiv.get_attribute("outerHTML"))