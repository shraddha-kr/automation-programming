import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

# def test_lamdatest_todo_app():
service = Service(executable_path="./chromedriver")
with webdriver.Chrome(service=service) as driver:

    driver.get("https://lambdatest.github.io/sample-todo-app/")
    driver.maximize_window()

    # chrome_driver.find_element_by_name("li1").click()
    # chrome_driver.find_element_by_name("li2").click()

    # title = "Sample page - lamdatest.com"
    # assert title == driver.title

    sample_text = "Happy testing at LambdaTest"
    email_text_field = driver.find_element_by_id("sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)

    output_str = driver.find_element_by_name("li6").text
    sys.stderr.write(output_str)
    sleep(2)
    driver.close()
