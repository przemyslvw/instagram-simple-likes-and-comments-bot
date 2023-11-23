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

    def __init__(self):
        print("sniffer run")


    def main(komunikat):
        print(komunikat)