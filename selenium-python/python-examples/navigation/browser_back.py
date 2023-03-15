from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="./chromedriver")
with webdriver.Chrome(service=service) as driver:
    driver.get("https://pythonexamples.org/")
    driver.find_element(By.LINK_TEXT, 'basics').click()
    driver.implicitly_wait(5)
    driver.back()
    driver.close()