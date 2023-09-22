from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_element(driver, by_locator):
    return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by_locator))
    
def get_element_text(driver, by_locator):
    return get_element(driver, by_locator).text