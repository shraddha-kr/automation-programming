# cmd [pytest -v test_demo.py]
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from support.common import get_element_text, get_element

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    # With the yield keyword, we return the driver object at the end of setup,  If the body of a def contains yield, 
    # the function automatically becomes a generator function
    yield driver
    driver.close()
    driver.quit()

# def test_open_url(driver):    
#     driver.get("https://google.com")
    
def test_verify_title(driver):        
    driver.get("http://dbankdemo.com/bank/login")
    assert "Digital Bank" == driver.title

def test_login(driver):
    # find username element input and type jsmith@demo.io
    driver.find_element(By.ID, 'username').send_keys('jsmith@demo.io')
    # find password element input and type Demo123!
    driver.find_element(By.ID, 'password').send_keys('Demo123!')
    # click sign-in button
    driver.find_element(By.ID, 'submit').click()
    assert 'home'in driver.current_url

def test_verify_version(driver):
    # click on about link button
    # driver.find_element(By.ID, 'aboutLink').click()    
    # verify version within the popup dialog
    # assert '2.1.0.11' in driver.find_element(By.CLASS_NAME, 'modal-body').text

    get_element(driver, (By.ID, 'aboutLink')).click()
    assert '2.1.0.11' in get_element_text(driver, (By.CLASS_NAME, 'modal-body'))

