from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

website = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(article_count.text)

# click on element
# article_count.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys("Python", Keys.ENTER)

input("Press 'ENTER' to close window")
