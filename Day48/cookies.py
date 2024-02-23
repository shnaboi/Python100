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

upg_cursor = driver.find_element(By.ID, 'buyCursor')
upg_granny = driver.find_element(By.ID, 'buyGrandma')
upg_factory = driver.find_element(By.ID, 'buyFactory')
upg_mine = driver.find_element(By.ID, 'buyMine')
upg_shipment = driver.find_element(By.ID, 'buyShipment')

game_on = True
def play_game():
  while game_on:
    cookie.click()

play_game()

toggle = input('ENTER to stop game')
game_on = False