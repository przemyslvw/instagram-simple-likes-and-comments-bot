import json
import argparse
from InstagramBot import InstagramBot

def load_comments():
    try:
        with open("comments.json", "r") as file:
            comments = json.load(file)
    except FileNotFoundError:
        comments = []
    return comments

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

def create_bot(account):
    bot = InstagramBot()
    bot.login(email=account["username"], password=account["password"])
    return bot

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
    loadcomments = load_comments()
    # print(loadcomments)
    # quit()
    # print(accounts[0])
    print(buffor)
    print(args.hashtag)


    # main functions / loading to buffor JSON
    bot = create_bot(accounts[0])
    # bot.scrape_hashtag_posts(args.hashtag)
    # bot.scrape_explore_posts(args.hashtag)
    bot.comment_on_posts(links=buffor, lcomments=loadcomments, delay_time=args.delay)
    # like and comment
    # InstagramBot().load_comments()


if __name__ == "__main__":
    main()
    print("END")