from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import js2py

service = Service(executable_path="./chromedriver")
with webdriver.Chrome(service=service) as driver:
    driver.get("https://datatables.net/extensions/select/examples/initialisation/checkbox.html")
    my_current_url = driver.current_url
    print(my_current_url)
    code = "alert('hello world');"
    res = js2py
    

    