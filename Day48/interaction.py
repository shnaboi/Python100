from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# website = "https://en.wikipedia.org/wiki/Main_Page"
#
# driver = webdriver.Chrome()
# driver.get(website)
# driver.maximize_window()
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#
# print(article_count.text)
#
# # click on element
# # article_count.click()
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys("Python", Keys.ENTER)
#
# input("Press 'ENTER' to close window")
#
driver = webdriver.Chrome()
driver.get('http://secure-retreat-92358.herokuapp.com/')
driver.maximize_window()

# time.sleep(3)

fname_field = driver.find_element(By.NAME, 'fName')
lname_field = driver.find_element(By.NAME, 'lName')
email_field = driver.find_element(By.NAME, 'email')
submit_btn = driver.find_element(By.XPATH, '/html/body/form/button')

fname_field.send_keys("shane", Keys.TAB)
lname_field.send_keys("kramer", Keys.TAB)
email_field.send_keys("beefyboy10@gmail.com")
submit_btn.click()

input("Press ENTER to close window")
