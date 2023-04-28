import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium driver\chromedriver_win32\chromedriver.exe")
driver.get("http://www.mitintech.com/webindex/")
driver.find_element(By.XPATH,'//label[@class="checkbtn"]/i').click()
driver.find_element(By.LINK_TEXT,'LOGIN').click()
extw=WebDriverWait(driver,2)


extw.until(expected_conditions.presence_of_element_located((By.NAME,'username'))).send_keys('kirtihinge')
#password
extw.until(expected_conditions.presence_of_element_located((By.NAME,'password'))).send_keys('prutha20')

extw.until(expected_conditions.element_located_to_be_selected((By.XPATH,'onclick="myFunction()"'))).click()

extw.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,'btn btn-primary px-5 text-bold'))).click()



