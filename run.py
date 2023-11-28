import json
import argparse
from InstagramBot import InstagramBot

def load_json(name):
    try:
        with open(name, "r") as file:
            json_content = json.load(file)
    except FileNotFoundError:
        json_content = []
    return json_content

def load_comments():
    comments = load_json("comments.json")
    return comments

def load_accounts():
    accounts = load_json("accounts.json")
    return accounts

def load_buffor():
    buffor = load_json("buffor.json")
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
    bot.scrape_hashtag_posts(args.hashtag)
    bot.scrape_explore_posts(args.hashtag)
    print(buffor)
    quit()
    bot.comment_on_posts(links=buffor, lcomments=loadcomments, delay_time=args.delay)
    # like and comment
    # InstagramBot().load_comments()


if __name__ == "__main__":
    main()
    print("END")