import time
import json
import random
#from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException

class SnifferBot:

    archiwum = []
    buffor = []

    def __init__(self):
        print("sniffer run")


    def load_archiwum(self):
        try:
            with open("archiwum.json", "r") as file:
                self.archiwum = json.load(file)
        except FileNotFoundError:
            self.archiwum = []

    def load_buffor(self):
        try:
            with open("buffor.json", "r") as file:
                self.buffor = json.load(file)
        except FileNotFoundError:
            self.buffor = []


    def main(self, posts):

        self.load_archiwum()
        self.load_buffor()

        for post in posts:
            print(post)
            print(self.archiwum)
            try:
                href = post.get_attribute("href")
                
                if href in self.archiwum: 
                    print("exist") 
                else: 
                    self.buffor.append(href)
                    self.archiwum.append(href)
                    
            except NoSuchElementException: 
                print("Href not exist")

            # save archiwum and bufor
        with open("archiwum.json", "w") as file:
            json.dump(self.archiwum, file)
        with open("buffor.json", "w") as file:
            json.dump(self.buffor, file)



