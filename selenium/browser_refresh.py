from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="./chromedriver")
with webdriver.Chrome(service=service) as driver:
    driver.get("https://pythonexamples.org/")
    driver.refresh()
    driver.close()


