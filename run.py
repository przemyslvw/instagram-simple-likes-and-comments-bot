import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# set driver options
chrome_options = Options()
chrome_options.add_argument("--window-size=930,820")
driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# main steps
driver.get("https://www.instagram.com")

print("Test 001")
time.sleep(10)

driver.close()