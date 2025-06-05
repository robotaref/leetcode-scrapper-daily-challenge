from scrapper import QuestionScrapper, DailyChallengeScrapper

import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--slug", help="your question slug")
argParser.add_argument("-d", "--daily", help="daily", action='store_true')

args = argParser.parse_args()

if args.slug:
    question_scrapper = QuestionScrapper()
    question_scrapper.scrape(args.slug)

elif args.daily:
    daily_scrapper = DailyChallengeScrapper()
    daily_scrapper.scrape(args.daily)

else:
    print("no command provided, refer to readme for available commands")
