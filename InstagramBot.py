import time
import random
import undetected_chromedriver as uc

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from SnifferBot import SnifferBot

class InstagramBot:

    def __init__(self):
        # print("Test 001")
        chrome_options = Options()
        chrome_options.add_argument("--window-size=930,820")
        # chrome_options.add_argument("--start-maximized")  # Maximize the Chrome window
        # Use webdriver_manager to automatically download and manage the ChromeDriver
        # add undetected_chromedriver here 
        self.driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    # cookies popup checker 
    def cookies_exist(self) -> bool:
   
        try:
            self.driver.find_element(By.CLASS_NAME, "_a9--")
            # print("True, jest like button zaznaczony")
            return True
            
        except NoSuchElementException: 
            # print("False, nie zaznaczone LIKE BUTTON")
            return False
        
    def cookies_checker(self):
        if self.cookies_exist():
            cookies_input = self.driver.find_element(By.CLASS_NAME, "_a9--")
            cookies_input.click()
            time.sleep(1)
        else:
            # print("cookies button not exist")
            None

        
    def scrape_explore_posts(self, hashtag):

        # Open Instagram and navigate to the hashtag page
        # print("Open Instagram explore page")

        time.sleep(1)
        self.driver.get(f"https://www.instagram.com/explore/")
        # Wait for the posts to load
        time.sleep(10)

        self.cookies_checker()

        most_recent = self.driver.find_element(By.CLASS_NAME, "x1gryazu")
        # Scrape the most recent posts from the hashtag
        posts = most_recent.find_elements(By.TAG_NAME, "a")
        # print(posts, "Links ready!")

        time.sleep(5)
        # sniffer run
        SnifferBot().main(posts)
        links = []
        for post in posts:
            # Retrieve the href attribute value
            href = post.get_attribute("href")
            # Process each href as needed
            links.append(href)
        
        # return links

    def scrape_hashtag_posts(self, hashtag):
        # Open Instagram and navigate to the hashtag page
        # print("Open Instagram and navigate to the hashtag page")

        time.sleep(1)
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        # Wait for the posts to load
        time.sleep(5)

        self.cookies_checker()

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_GQ"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div')))
        most_recent = self.driver.find_element(By.CLASS_NAME, "_ac7v")
        # Scrape the most recent posts from the hashtag
        posts = most_recent.find_elements(By.TAG_NAME, "a")
        # print(posts, "Links ready!")

        time.sleep(5)
        # sniffer run
        SnifferBot().main(posts)
        links = []
        for post in posts:
            # Retrieve the href attribute value
            href = post.get_attribute("href")
            # Process each href as needed
            links.append(href)
        # return links

    # check like button
    def like_exist(self) -> bool:

        try:
            # self.driver.find_element(By.CLASS_NAME, "xp7jhwk")
            self.driver.find_element(By.XPATH, "//*[name()='svg' and @aria-label='Nie lubię']")
            # print("True, jest like button zaznaczony")
            return True
            
        except NoSuchElementException: 
            # print("False, nie zaznaczone LIKE BUTTON")
            return False

    # check comment area
    def comment_exist(self) -> bool:
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Dodaj komentarz..."]')
            # print("True, jest comment area")
            return True
        except NoSuchElementException: 
            # print("False, nie ma comment area")
            return False
               
    def login(self, email, password):
        # print("login page")
        # Open Instagram
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        # Wait for the login elements to become available
        wait = WebDriverWait(self.driver, 10)
        # Find the cookies button
        self.cookies_checker()

        email_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        # Find the login elements and enter email and password
        email_field.send_keys(email)
        password_field.send_keys(password)

        # # Submit the login form
        password_field.send_keys(Keys.RETURN)


        # Wait for the login process to complete (you may need to adjust the delay based on your internet speed)
        time.sleep(5)  # Wait for 5 seconds (adjust as needed)

        # self.driver.quit()
    
    def comment_on_posts(self, links, lcomments, delay_time):

        for link in links:
            # Open each post link
            comments = lcomments
            comment = random.choice(comments)
            emois = [" 👍", " 🔥", " 👌", " 💎", " 🌟", " 😍"]
            emoi = random.choice(emois)
            self.driver.get(link)

            time.sleep(5)
            
            # Find the comment input field
            if self.like_exist():
                # print("zaznaczony")
                SnifferBot().save_to_archiwum(link)
            else:
                try:
                    like_input = self.driver.find_element(By.CLASS_NAME, "xp7jhwk")
                    like_input.click()
                except NoSuchElementException:
                    print("Element .xp7jhwk does not exist, continuing...")
                time.sleep(2)

                if self.comment_exist():
                    comment_input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Dodaj komentarz..."]')
                    comment_input.click()
                    time.sleep(2)
                    # Create an instance of ActionChains
                    actions = ActionChains(self.driver)
                    actions.send_keys(comment+emoi)
                    actions.send_keys(Keys.RETURN)
                    # Perform the actions
                    actions.perform()
                else:
                    # print("comment imput not exist")
                    None

            try:
                most_recent = self.driver.find_element(By.CLASS_NAME, "_ac7v")
                # Scrape the most recent posts from the hashtag
                posts = most_recent.find_elements(By.TAG_NAME, "a")
                # print(posts, "Bottom links ready!")
                for post in posts:
                    # Retrieve the href attribute value
                    try:
                        # print(post.get_attribute("href"))
                
                        SnifferBot().save_to_buffor(post.get_attribute("href"))
                            
                    except NoSuchElementException: 
                        # print("Href not exist")
                        None

            except NoSuchElementException: 
                # print("False, bottom area false")
                None
                
            # after add comment save link to arhivum
            SnifferBot().save_to_archiwum(link)

        time.sleep(delay_time)


    # self.driver.quit()
    
    time.sleep(5)