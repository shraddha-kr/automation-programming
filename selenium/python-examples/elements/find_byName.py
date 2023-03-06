from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('http://127.0.0.1:5500/localwebsite/index.html')
    # find element by name
    # <div name="xyz">Read More</div>
    myDiv = driver.find_element(By.NAME, 'xyz')
    print(myDiv)
    print(myDiv.text)