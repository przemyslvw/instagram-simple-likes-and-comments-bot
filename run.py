import argparse
import json
from InstagramBot import InstagramBot

def load_accounts():
    print("test 003")
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
            print(accounts)
    except FileNotFoundError:
        accounts = []
    return accounts

def main():

    # init parser
    parser = argparse.ArgumentParser(description="Instagram Bot")
    # parser options
    parser.add_argument("-ht", "--hashtag", help="Hashtag to scrape posts from")
    parser.add_argument("-cm", "--message", help="Comment or message to post")
    parser.add_argument("-del", "--delay", type=int, default=5, help="Delay in seconds between actions")

    args = parser.parse_args()

    # def start_bot():
    accounts = load_accounts()
    if len(accounts) == 0:
        print("end", "No accounts found. Please add accounts first.\n")
        return
    else:
        print("account exist")

    args = parser.parse_args()
    print(args.hashtag)

if __name__ == "__main__":
    main()