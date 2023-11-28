import json
from selenium.common.exceptions import NoSuchElementException 

class SnifferBot:

    archiwum = []
    buffor = []

    def __init__(self):
        # print("sniffer run")
        None

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

    def save_to_archiwum(self, href):
        self.load_archiwum()
        self.load_buffor()
        self.archiwum.append(href)
        with open("archiwum.json", "w") as file:
            json.dump(self.archiwum, file)
        if href in self.buffor: 
            self.buffor.remove(href)
            with open("buffor.json", "w") as file:
                json.dump(self.buffor, file)
        else:
            None

    def save_to_buffor(self, href):
        self.load_archiwum()
        self.load_buffor()

        try:    
            if href in self.archiwum or href in self.buffor: 
                # print("exist") 
                if href in self.buffor: 
                    self.buffor.remove(href)
                    with open("buffor.json", "w") as file:
                        json.dump(self.buffor, file)
                else:
                    None
                #     print("not exist in buffor")
            else: 
                self.buffor.append(href)
                with open("buffor.json", "w") as file:
                    json.dump(self.buffor, file)
        except NoSuchElementException: 
            # print("Href not exist")
            None


    def main(self, posts):

        self.load_archiwum()
        self.load_buffor()

        for post in posts:
            # print(post)
            # print(self.archiwum)
            try:
                href = post.get_attribute("href")
                
                if href in self.archiwum: 
                    # print("exist") 
                    if href in self.buffor: 
                        self.buffor.remove(href)
                    else:
                        # print("nie ma w buforze")
                        None
                else: 
                    self.buffor.append(href)

            except NoSuchElementException: 
                # print("Href not exist")
                None

            # save archiwum and bufor
        with open("buffor.json", "w") as file:
            json.dump(self.buffor, file)



