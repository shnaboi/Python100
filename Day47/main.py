from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

amazon_product = "https://www.amazon.com/Yonex-EZONE-Night-Tennis-Racquet/dp/B0CS8DQGT3/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=GpDMq&content-id=amzn1.sym.225b4624-972d-4629-9040-f1bf9923dd95%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=225b4624-972d-4629-9040-f1bf9923dd95&pf_rd_r=9MC9ZZW3Q566XV9GMD3M&pd_rd_wg=DWAor&pd_rd_r=7725b019-8907-4ca2-a152-f68bde23231d&pd_rd_i=B0CS8DCPRQ&th=1"

# Create ChromeOptions object
chrome_options = Options()

# Enable headless mode
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--enable-javascript")

# Create a WebDriver instance
driver = webdriver.Chrome(options=chrome_options)  # Use ChromeDriver (or any other WebDriver)

# Navigate to the Amazon product page
driver.get(amazon_product)
print("line 28")

try:
  price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")

  print("try succeeded")
  # Extract the price text
  price = price_element.text
  print('Price:', price)
finally:
  # Close the WebDriver
  driver.quit()
