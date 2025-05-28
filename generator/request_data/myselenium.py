from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()
# Add your options as needed
options = [
   # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    # These flags BELOW are recommended for stability when running Chrome in headless or containerized environments (such as GitHub Actions).
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222'
]
for option in options:
    chrome_options.add_argument(option)


def get(url):
  driver = webdriver.Chrome(options = chrome_options)
  driver.get(url)
  #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kw")))
  driver.implicitly_wait(10)
  print(driver.title)
  return driver

