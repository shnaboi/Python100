from selenium import webdriver
from selenium.webdriver.common.by import By

website = "https://www.python.org/"

driver = webdriver.Chrome()

driver.get(website)
events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/h2')

print(events.text)

