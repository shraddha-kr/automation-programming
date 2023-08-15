# cmd [pytest -v test_demo.py]
from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    # With the yield keyword, we return the driver object at the end of setup,  If the body of a def contains yield, 
    # the function automatically becomes a generator function
    yield driver
    driver.close()
    driver.quit()


def test_open_url(driver):    
    driver.get("https://google.com")
    
def test_verify_title(driver):        
    driver.get("http://dbankdemo.com/bank/login")
    assert "Digital Bank"