from selenium import webdriver

driver = webdriver.Firefox(executable_path="./geckodriver.exe")
driver.get("https://www.softwaretestingmaterial.com/")