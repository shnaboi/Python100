from selenium import webdriver
from selenium.webdriver.common.by import By

website = "https://www.python.org/"

driver = webdriver.Chrome()

driver.get(website)
events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

li_items = events.find_elements(By.TAG_NAME, "li")
num = 1
dates_lib = {}
for li in li_items:
  text = li.text.split("\n")
  info_to_append = {
    num: {
      "Date": text[0],
      "Name": text[1]
    }
  }
  dates_lib.update(info_to_append)
  num += 1

print(dates_lib)

