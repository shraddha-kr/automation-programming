import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
test_url = "https://www.w3schools.com/html/html_tables.asp"
 
class WebTableTest(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
 
    def test_1_get_num_rows_(self):
        driver = self.driver
        driver.get(test_url)
        
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))       
        num_rows = len (driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        print("Rows in table are " + repr(num_rows))
 
    def test_2_get_num_cols_(self):
        driver = self.driver
        driver.get(test_url)
        
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))        
        num_cols = len (driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td"))
        print("Columns in table are " + repr(num_cols))
 
    def test_3_get_col_headers(self):
        driver = self.driver
        driver.get(test_url)
        
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))
        header_list = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th")
        for i in header_list:
            print(i.text)

    def test_4_get_row_data(self):
        driver = self.driver
        driver.get(test_url)
        
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))
        # since row 1 is the header details
        row_data = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td")
        for i in row_data:
            print(i.text)

    def test_5_get_col_data(self):
        driver = self.driver
        driver.get(test_url)
        
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))
        # since row 1 is the header details
        col_data = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/td[3]")
        for i in col_data:
            print(i.text)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
 
if __name__ == "__main__":
    unittest.main()