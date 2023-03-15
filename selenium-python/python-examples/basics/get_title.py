from selenium.webdriver.chrome.service import Service
from selenium import webdriver


service = Service(executable_path="./chromedriver")
with webdriver.Chrome(service=service) as driver:
    driver.get("https://pythonexamples.org/")
    my_title = driver.title
    print(my_title)
    driver.close()