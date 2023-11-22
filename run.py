import argparse
import json
from InstagramBot import InstagramBot

def load_accounts():
    print("test 003")
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
    except FileNotFoundError:
        accounts = []
    return accounts

# Create Object Instagram Bot / return bot
def create_bot(account):
    bot = InstagramBot()
    bot.login(email=account["username"], password=account["password"])
    print("Test 003")
    return bot

def main():

    # init parser
    parser = argparse.ArgumentParser(description="Instagram Bot")
    # parser options
    parser.add_argument("-ht", "--hashtag", help="Hashtag to scrape posts from")
    parser.add_argument("-cm", "--message", help="Comment or message to post")
    parser.add_argument("-del", "--delay", type=int, default=5, help="Delay in seconds between actions")

    args = parser.parse_args()

    print("Test 002")
    # def start_bot():
    accounts = load_accounts()
    if len(accounts) == 0:
        print("end", "No accounts found. Please add accounts first.\n")
        return
    else:
        print("account exist")

    args = parser.parse_args()
    hashtag = args.hashtag

    create_bot(accounts[0])
    # bot.login(links=post_links, comment=args.comment, delay_time=args.delay)

if __name__ == "__main__":
    main()
    print("Test 005")