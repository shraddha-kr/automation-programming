# https://www.softwaretestingmaterial.com/how-to-handle-web-tables-in-selenium-python/
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=".\chromedriver.exe")
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")

# l = driver.find_element(By.XPATH, "//*[@class= 'spTable']/tbody/tr[3]/td[2]")
num_rows = len(driver.find_element(By.XPATH, "//*[@class= 'spTable']/tbody/tr"))
print(num_rows)

driver.quit()