from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

amazon_product = "https://www.amazon.com/Yonex-EZONE-Night-Tennis-Racquet/dp/B0CS8H2JK5/ref=sr_1_4?crid=3464C3IPN9Y8E&dib=eyJ2IjoiMSJ9.MU1l-1BxejHTLYnrshhp3iOu7NQ1dk0KsQijbfTzDpWz2otfjLwilTy_xQM6Va0XcrOktlZmPZIyTECz4fhCwDf-xGkIvZxhlMuZYH5Ee4YcZCZo7WMFnr2b36z0spPobKE3rOkN_88bcODThuckk7pYLfTFEGMhET-nyL4TwJAXjQC8QaOcsH6r95s8l1wHsSlgjXL_4wXrGM3vJCw9rUfb9mip6r8TZxkysknDxnDBrJd1k3FKfo6sH5LJnugJ-R6aM6MVSyYgyrQPHcSWXxSEwTRM5ASUEAWoM0A5mCw.TOBxZ7HwuyfJT9tR8omT622VKA2c-icM7uoZhk-iqLQ&dib_tag=se&keywords=yonex%2Bezone%2Bblack&qid=1708361700&sprefix=yonex%2Bezone%2Bbla%2Caps%2C169&sr=8-4&th=1"

header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
  "Accept-Language": "en-US,en;q=0.9"
}

# Create a WebDriver instance
driver = webdriver.Chrome()  # Use ChromeDriver (or any other WebDriver)

# Navigate to the Amazon product page
driver.get(amazon_product)

try:
    # Wait for the price element to be visible
    price_element = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'a-price-whole'))
    )

    # Extract the price text
    price = price_element.text
    print('Price:', price)
finally:
    # Close the WebDriver
    driver.quit()


# response = requests.get(amazon_product, headers=header)
# webpage = response.text
# soup = BeautifulSoup(webpage, "lxml")
#
# print(soup)