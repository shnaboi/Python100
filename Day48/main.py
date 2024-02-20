from selenium import webdriver
from selenium.webdriver.common.by import By

website = "https://www.python.org/"

driver = webdriver.Chrome()

driver.get(website)
events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

li_items = events.find_elements(By.TAG_NAME, "li")
num = 1
for li in li_items:
  date_and_title = li.text
  print(f"{num}: {date_and_title}")
  num += 1


