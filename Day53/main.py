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
print(houses)

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

