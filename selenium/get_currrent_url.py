from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="./chromedriver")
with webdriver.Chrome(service=service) as driver:
    driver.get("https://pythonexamples.org/")
    my_current_url = driver.current_url
    print(my_current_url)
    driver.find_element(By.LINK_TEXT, "Python Examples").click()
    driver.implicitly_wait(5)
    driver.close()
    