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

def add_comment(message):
        comments = load_comments()
        if message in comments: 
            None
        else:
            comments.append(message)
            with open("comments.json", "w") as file:
                json.dump(comments, file)

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

    if type(args.message) == str:
        add_comment(args.message)
    else:
        None
    # quit()
    # print(accounts[0])
    # print(buffor)
    # print(args)


    # main functions / loading to buffor JSON
    bot = create_bot(accounts[0])
    if type(args.message) == str:
        bot.scrape_hashtag_posts(args.hashtag)
    else:
        bot.scrape_explore_posts(args.hashtag)
    # bot.scrape_explore_posts(args.hashtag)
    # print(len(load_buffor()))
    while (len(load_buffor()) >= 0):
        print("new loop")
        if len(load_buffor()) == 0:
            bot.scrape_explore_posts(args.hashtag)
            if type(args.message) == str:
                bot.scrape_hashtag_posts(args.hashtag)
            else:
                None
        else:
            None

        bot.comment_on_posts(links=load_buffor(), lcomments=loadcomments, delay_time=args.delay)
    # like and comment
    # InstagramBot().load_comments()


if __name__ == "__main__":
    main()
    print("END")
    quit()