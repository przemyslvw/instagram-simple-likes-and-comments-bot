import time

import undetected_chromedriver as uc

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class InstagramBot:

    print("Test 001")
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=930,820")
        # chrome_options.add_argument("--start-maximized")  # Maximize the Chrome window
        # Use webdriver_manager to automatically download and manage the ChromeDriver
        # add undetected_chromedriver here 
        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # cookies popup checker 
    def cookies_exist(self) -> bool:
        wait = WebDriverWait(self.driver, 10)
        cookies = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_a9--")))
        try: 
            cookies
            return True
            
        except:
            return False
        
    def login(self, email, password):
        # Open Instagram
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        # Wait for the login elements to become available
        wait = WebDriverWait(self.driver, 10)
        # Find the cookies button
        if self.cookies_exist():
            cookies_input = self.driver.find_element(By.CLASS_NAME, "_a9--")
            cookies_input.click()
            time.sleep(1)
        else:
            print("cookies button not exist")
        time.sleep(5)

        email_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        # Find the login elements and enter email and password
        email_field.send_keys(email)
        password_field.send_keys(password)

        # # Submit the login form
        # password_field.send_keys(Keys.RETURN)

        # Wait for the login process to complete (you may need to adjust the delay based on your internet speed)
        time.sleep(5)  # Wait for 5 seconds (adjust as needed)

    
    time.sleep(10)