from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = r"C:\Users\theor\OneDrive\Documents\CITS3403\CITS3403-Website-Project\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/")
print(driver.title)
time.sleep(5)

driver.get("http://127.0.0.1:5000/user")
print(driver.title)
time.sleep(5)

driver.get("http://127.0.0.1:5000/statistics")
print(driver.title)
time.sleep(5)

driver.get("http://127.0.0.1:5000/assessment")
print(driver.title)
time.sleep(5)

driver.get("http://127.0.0.1:5000/login")
print(driver.title)
time.sleep(5)

driver.get("http://127.0.0.1:5000/signup")
print(driver.title)
time.sleep(5)

driver.get("http://127.0.0.1:5000/admin")
print(driver.title)
time.sleep(5)

driver.get("http://127.0.0.1:5000/adminAssessment")
print(driver.title)
time.sleep(5)

driver.get("http://127.0.0.1:5000/adminUser")
print(driver.title)
time.sleep(5)
#for input objects
#search = driver.find_elemtn_by_id(idname)
#search.send_keys('text to input')
#search.sen_keys(Keys.RETURN)

driver.quit()