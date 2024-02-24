from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

website = 'https://orteil.dashnet.org/experiments/cookie/'

driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()

time.sleep(1)

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

game_on = True
start_time = time.time()
timeout = 5

def play_game():
  while game_on:
    cookie.click()
    money = int((driver.find_element(By.ID, 'money').text).replace(",", ""))
    check_upg(money)

def check_upg(money):
  # get prices of items and put into list
  prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
  item_prices = []
  for item in prices:
    text = item.text
    if text != '':
      cost = int(text.split("-")[1].strip().replace(",", ""))
      item_prices.append(cost)

  # create dict of upgrades to evaluate
  upgrades = {}
  for n in range(len(item_prices)):
    upgrades[item_prices[n]] = item_ids[n]
  affordable = {}
  for cost, id in upgrades.items():
    if money > cost:
      affordable[cost] = id

  print(upgrades)

  best_choice = max(affordable)
  purchase_id = affordable[best_choice]

  driver.find_element(By.ID, purchase_id).click()



# def game_cycle():
#   upg_factory = driver.find_element(By.ID, 'buyFactory')
#   upg_mine = driver.find_element(By.ID, 'buyMine')
#   upg_shipment = driver.find_element(By.ID, 'buyShipment')
#   upg_alchemy = driver.find_element(By.ID, 'buyAlchemy lab')
#
#   # get html elements class
#   factory_class = upg_factory.get_attribute("class")
#   mine_class = upg_mine.get_attribute("class")
#   shipment_class = upg_shipment.get_attribute("class")
#   alchemy_class = upg_alchemy.get_attribute("class")
#
#   b_mine = upg_mine.find_element(By.TAG_NAME, "b").text
#   mine_cost = float(''.join(num for num in b_mine if num.isdigit()))
#   b_shipment = upg_shipment.find_element(By.TAG_NAME, "b").text
#   shipment_cost = float(''.join(num for num in b_shipment if num.isdigit()))
#   b_alchemy = upg_alchemy.find_element(By.TAG_NAME, "b").text
#   alchemy_cost = float(''.join(num for num in b_alchemy if num.isdigit()))
#
#   cps = driver.find_element(By.ID, 'cps').text
#   cps_num = float(''.join(num for num in cps if num.isdigit()))
#   money = float((driver.find_element(By.ID, 'money').text).replace(",", ""))
#
#   if money + cps_num * 17 + 850 >= alchemy_cost:
#     while alchemy_class:
#       cookie.click()
#       alchemy_class = upg_alchemy.get_attribute("class")
#     upg_alchemy.click()
#   elif money + cps_num * 11 + 550 >= shipment_cost:
#     while shipment_class:
#       cookie.click()
#       shipment_class = upg_shipment.get_attribute("class")
#     upg_shipment.click()
#   elif money + cps_num * 7 + 350 >= mine_cost:
#     while mine_class:
#       cookie.click()
#       mine_class = upg_mine.get_attribute("class")
#     upg_mine.click()
#   else:
#     while factory_class:
#       cookie.click()
#       factory_class = upg_factory.get_attribute("class")
#     upg_factory.click()

  # if (money + cps_num + 50 >= factory_cost):
  #   while not factory_class:
  #     cookie.click()
  #   # check cost of mines and time to meet cost
  #   if (money + (cps_num * 3) + 150) >= mine_cost:
  #     while not mine_class:
  #       cookie.click()
  #     upg_mine.click()
  #   else:
  #     upg_factory.click()
  # else:
  #   while not factory_class:
  #     cookie.click()
  #   upg_factory.click()
  # game_cycle()

# def check_upgrades():
#   # get html elements
#   upg_granny = driver.find_element(By.ID, 'buyGrandma')
#   upg_factory = driver.find_element(By.ID, 'buyFactory')
#   upg_mine = driver.find_element(By.ID, 'buyMine')
#   upg_shipment = driver.find_element(By.ID, 'buyShipment')
#
#   # get html elements class
#   granny_class = upg_granny.get_attribute("class")
#   factory_class = upg_factory.get_attribute("class")
#   mine_class = upg_mine.get_attribute("class")
#   shipment_class = upg_shipment.get_attribute("class")
#
#   cps = driver.find_element(By.ID, 'cps').text
#   cps_num = float(''.join(num for num in cps if num.isdigit()))
#
#   money = float((driver.find_element(By.ID, 'money').text).replace(",", ""))
#
#   b_factory = upg_factory.find_element(By.TAG_NAME, "b").text
#   factory_cost = float(''.join(num for num in b_factory if num.isdigit()))
#   b_mine = upg_mine.find_element(By.TAG_NAME, "b").text
#   mine_cost = float(''.join(num for num in b_mine if num.isdigit()))
#   b_shipment = upg_shipment.find_element(By.TAG_NAME, "b").text
#   shipment_cost = float(''.join(num for num in b_shipment if num.isdigit()))
#
#   if (cps_num + money + 650) >= shipment_cost:
#     upg_time = time.time() + 11
#     while time.time() < upg_time:
#       cookie.click()
#     upg_shipment.click()
#     print('ship worth it')
#   elif (cps_num + money + 300) >= mine_cost:
#     upg_time = time.time() + 5
#     while time.time() < upg_time:
#       cookie.click()
#     upg_mine.click()
#     print('mine worth it')
#   elif (cps_num + money + 55) >= factory_cost:
#     upg_time = time.time() + 1
#     while time.time() < upg_time:
#       cookie.click()
#     upg_factory.click()
#     print("factory worth it")
#   elif not shipment_class:
#     upg_shipment.click()
#     print('normal')
#   elif not mine_class:
#     upg_mine.click()
#     print('normal')
#   elif not factory_class:
#     upg_factory.click()
#     print('normal factory')
#   elif not granny_class:
#     upg_granny.click()
#     print('normal')
#   play_game()

# REORGANIZE ALGORITHM SO THAT UPG ARE MADE AS SOON AS THEY ARE AVAILABLE
# ALSO REORGANIZE SO THAT ALGORITHM IS NOT ALWAYS WAITING EXTRA SECONDS BY DEFAULT TO MAKE PURCHASES IT CAN ALREADY MAKE


play_game()