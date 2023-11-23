import argparse
from InstagramBot import InstagramBot

def main():

    # init parser
    parser = argparse.ArgumentParser(description="Instagram Bot")
    # parser options
    parser.add_argument("-ht", "--hashtag", help="Hashtag to scrape posts from")
    parser.add_argument("-cm", "--message", help="Comment or message to post")
    parser.add_argument("-del", "--delay", type=int, default=5, help="Delay in seconds between actions")
    args = parser.parse_args()

    # main functions / loading to buffor JSON
    InstagramBot().scrape_hashtag_posts(args.hashtag)
    InstagramBot().scrape_explore_posts(args.hashtag)
    # like and comment
    InstagramBot().load_comments()


if __name__ == "__main__":
    main()
    print("END")