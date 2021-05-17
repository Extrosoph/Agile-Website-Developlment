from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = r"C:\Users\theor\OneDrive\Documents\CITS3403\CITS3403-Website-Project\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/")
driver.find_element_by_id('loginpage').click()

# Insert the admin username and password
username = driver.find_element_by_id('email')
password = driver.find_element_by_id('passwordInput')
username.send_keys('admin')
password.send_keys('admin')
time.sleep(2)

# Log into the admin account
driver.find_element_by_id('login').click()
time.sleep(10)

# Close browser
driver.quit()