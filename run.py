import json
import argparse
from InstagramBot import InstagramBot

def load_accounts():
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
    except FileNotFoundError:
        accounts = []
    return accounts

def load_buffor():
    try:
        with open("buffor.json", "r") as file:
            buffor = json.load(file)
    except FileNotFoundError:
        buffor = []
    return buffor

def main():

    # init parser
    parser = argparse.ArgumentParser(description="Instagram Bot")
    # parser options
    parser.add_argument("-ht", "--hashtag", help="Hashtag to scrape posts from")
    parser.add_argument("-cm", "--message", help="Comment or message to post")
    parser.add_argument("-del", "--delay", type=int, default=5, help="Delay in seconds between actions")
    args = parser.parse_args()
    accounts = load_accounts()
    buffor = load_buffor()

    print(accounts[0])
    print(buffor)


    # main functions / loading to buffor JSON
    # bot = create_bot(accounts[0])
    # bot.scrape_hashtag_posts(args.hashtag)
    # bot.scrape_explore_posts(args.hashtag)
    # like and comment
    # InstagramBot().load_comments()


if __name__ == "__main__":
    main()
    print("END")