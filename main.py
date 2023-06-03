from scrapper.scrapper import QuestionScrapper, DailyChallengeScrapper

import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--slug", help="your question slug")
argParser.add_argument("-d", "--daily", help="daily")

args = argParser.parse_args()

if args.slug:
    question_scrapper = QuestionScrapper(args.slug)

    question_scrapper.scrape()

elif args.daily:
    daily_scrapper = DailyChallengeScrapper()
    question_slug = daily_scrapper.get_daily_question_slug()
    question_scrapper = QuestionScrapper(question_slug)
    question_scrapper.scrape()
