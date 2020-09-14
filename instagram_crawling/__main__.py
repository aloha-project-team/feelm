import collection.crawler as crawler
import datetime

if __name__ == '__main__':
    print("__main__.py is running...")
    until=datetime.datetime.now()
    since=until-datetime.timedelta(days=30)

    items = [
        {
            #token_user
            'pagename':'me',
            'since': since.strftime("%Y-%m-%d"),
            'until': until.strftime("%Y-%m-%d"),
        },
    ]

    for item in items:
        crawler.crawling(**item)