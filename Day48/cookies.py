from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

website = 'https://orteil.dashnet.org/experiments/cookie/'

driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()

time.sleep(3)

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

game_on = True
def play_game():
  timeout = time.time() + 3
  while game_on:
    cookie.click()
    if time.time() > timeout:
      break
  check_upgrades()

def check_upgrades():
  # get upgrade elements
  upg_cursor = driver.find_element(By.ID, 'buyCursor')
  upg_granny = driver.find_element(By.ID, 'buyGrandma')
  upg_factory = driver.find_element(By.ID, 'buyFactory')
  upg_mine = driver.find_element(By.ID, 'buyMine')
  upg_shipment = driver.find_element(By.ID, 'buyShipment')

  # get upgrade elements class
  granny_val = upg_granny.get_attribute("class")
  factory_val = upg_factory.get_attribute("class")
  mine_val = upg_mine.get_attribute("class")
  shipment_val = upg_shipment.get_attribute("class")

  if not shipment_val:
    upg_shipment.click()
  elif not mine_val:
    upg_mine.click()
  elif not factory_val:
    upg_factory.click()
  elif not granny_val:
    upg_granny.click()
  else:
    upg_cursor.click()
  play_game()


play_game()