from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

website = 'https://orteil.dashnet.org/experiments/cookie/'

driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()

time.sleep(2)

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

game_on = True
start_time = time.time()
timeout = 5

def play_game():
  timeout = time.time() + 5
  num = 0
  while game_on:
    cookie.click()
    num += 1
    if time.time() > timeout:
      break
  check_upgrades()

def check_upgrades():
  # get html elements
  upg_cursor = driver.find_element(By.ID, 'buyCursor')
  upg_granny = driver.find_element(By.ID, 'buyGrandma')
  upg_factory = driver.find_element(By.ID, 'buyFactory')
  upg_mine = driver.find_element(By.ID, 'buyMine')
  upg_shipment = driver.find_element(By.ID, 'buyShipment')

  # get html elements class
  granny_class = upg_granny.get_attribute("class")
  factory_class = upg_factory.get_attribute("class")
  mine_class = upg_mine.get_attribute("class")
  shipment_class = upg_shipment.get_attribute("class")

  cps = driver.find_element(By.ID, 'cps').text
  cps_string = ''.join(num for num in cps if num.isdigit())
  cps_num = float(cps_string)

  money = float((driver.find_element(By.ID, 'money').text).replace(",", ""))

  b_cursor = upg_cursor.find_element(By.TAG_NAME, "b").text
  cursor_cost = float(''.join(num for num in b_cursor if num.isdigit()))
  b_granny = upg_granny.find_element(By.TAG_NAME, "b").text
  granny_cost = float(''.join(num for num in b_granny if num.isdigit()))
  b_factory = upg_factory.find_element(By.TAG_NAME, "b").text
  factory_cost = float(''.join(num for num in b_factory if num.isdigit()))
  b_mine = upg_mine.find_element(By.TAG_NAME, "b").text
  mine_cost = float(''.join(num for num in b_mine if num.isdigit()))
  b_shipment = upg_shipment.find_element(By.TAG_NAME, "b").text
  shipment_cost = float(''.join(num for num in b_shipment if num.isdigit()))

  if (cps_num + money + 300) >= shipment_cost:
    upg_time = time.time() + 5
    while time.time() < upg_time:
      cookie.click()
    upg_shipment.click()
    print('ship worth it')
  elif (cps_num + money + 150) >= mine_cost:
    upg_time = time.time() + 3
    while time.time() < upg_time:
      cookie.click()
    upg_mine.click()
    print('mine worth it')
  elif (cps_num + money + 55) >= factory_cost:
    upg_time = time.time() + 1
    while time.time() < upg_time:
      cookie.click()
    upg_factory.click()
    print("factory worth it")
  elif not shipment_class:
    upg_shipment.click()
  elif not mine_class:
    upg_mine.click()
  elif not factory_class:
    upg_factory.click()
  elif not granny_class:
    upg_granny.click()
  else:
    upg_cursor.click()
  play_game()


play_game()