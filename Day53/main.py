import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

zillow_site = 'https://appbrewery.github.io/Zillow-Clone/'
google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSdP5ix5nzqecYF3qubOu1plWqJ1NbojMw1SDihTNkXj-mzmow/viewform?usp=sf_link'
google_form_responses = "https://docs.google.com/spreadsheets/d/1Zxe6KNI28u6XjhhbVuysiM220PL53FkvJXxtizrVoeQ/edit?resourcekey#gid=797115165"

# info is div class="StyledPropertyCardDataWrapper"

response = requests.get(zillow_site)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
houses = soup.find_all(name='div', class_="StyledPropertyCardDataWrapper")
# print(houses)

list = []
for house in houses:
  link = house.find_next("a", class_="StyledPropertyCardDataArea-anchor").get_attribute_list("href")[0]
  address = house.find_next("address").get_text().strip()
  price_string = house.find_next("span").get_text()
  price = int(''.join(x for x in price_string if x.isdigit()))
  listing = [address, price, link]
  list.append(listing)
  # print(listing)

driver = webdriver.Chrome()
driver.get(google_form)

time.sleep(1)

for rental in list:
  input_address = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
  input_price = driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
  input_link = driver.find_element(By.XPATH,
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
  submit_butt = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

  time.sleep(1)
  input_address.send_keys(rental[0])
  input_price.send_keys(rental[1])
  input_link.send_keys(rental[2])
  submit_butt.click()
  time.sleep(1)
  submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
  submit_another.click()


"""
Use BeautifulSoup/Requests to scrape all the listings from the Zillow-Clone web address (Step 4 above).

Create a list of links for all the listings you scraped. e.g.

Create a list of prices for all the listings you scraped. e.g.

Clean up the strings, by removing any "+" symbols and other information so that you are only left with a dollar price. 
The price should look like "$1,234" instead of "$1,234+ /mo"

Clean up the address data as well. Remove any newlines, pipe symbols |, and unnecessary whitespace



Selenium Requirements



Use Selenium to fill in the form you created (step 1,2,3 above). 
Each listing should have its price/address/link added to the form. 
You will need to fill in a new form for each new listing.

Once all the data has been filled in, 
click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. 
You should end up with a spreadsheet with all the details from the properties.



"""

