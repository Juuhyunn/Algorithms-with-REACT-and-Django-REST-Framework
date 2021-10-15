import numpy as np
from icecream import ic
import pandas as pd
from sklearn import preprocessing
from admin.common.models import ValueObject, Printer, Reader
import csv
import datetime as dt
from bs4 import BeautifulSoup
from selenium import webdriver
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re

class Crawling(object):
    def __init__(self):
        pass

    def process(self):
        self.naver_movie()

    def naver_movie(self):
        vo = ValueObject()
        vo.context = 'admin/crawling/data'
        vo.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver')
        driver.get(vo.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': 'tit3'})
        arr = [div.a.string for div in all_div]
        # [print(i) for i in arr]
        driver.close()
        # dt = dict(zip([i for i in range(1, len(arr)+1)], arr))
        # ic(dt)
        # with open(f'{vo.context}/rank_movies.csv', 'w', encoding='UTF-8') as f:
        #     w = csv.writer(f)
        #     # w.writerow(dt.keys())
        #     # w.writerow(dt.values())
        #     [w.writerow([i, dt[i]]) for i in range(1, len(dt)+1)]
        with open(f'{vo.context}/rank_movies.csv', 'w', encoding='UTF-8') as f:
            w = csv.writer(f)
            [w.writerow([i+1, arr[i]]) for i in range(len(arr))]
        # dt = dict(zip([i for i in range(1, len(arr)+1)], arr))
        # df = pd.DataFrame.from_dict(dt, orient='index', columns=['이름'])
        # df.to_csv(f'{vo.context}/rank_movies.csv')

    def tweet_trump(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome('admin/crawling/data/chromedriver', options=options)

        start_date = dt.date(year=2018, month=12, day=1)
        until_date = dt.date(year=2018, month=12, day=2)  # 시작날짜 +1
        end_date = dt.date(year=2018, month=12, day=2)
        query = 'Donald Trump'
        total_tweets = []
        url = f'https://twitter.com/search?q={query}%20' \
              f'since%3A{str(start_date)}%20until%3A{str(until_date)}&amp;amp;amp;amp;amp;amp;lang=eg'
        while not end_date == start_date:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                daily_freq = {'Date': start_date}
                word_freq = 0
                tweets = soup.find_all('p', {'class': 'TweetWextSize'})
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                new_height = driver.execute_script('return document.body.scrollHeight')
                if new_height != last_height:
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    tweets = soup.find_all('p', {'class', 'TweetTextSize'})
                    word_freq = len(tweets)
                else:
                    daily_freq['Frequency'] = word_freq
                    word_freq = 0
                    start_date = until_date
                    until_date = dt.timedelta(days=1)
                    daily_freq = {}
                    total_tweets.append(tweets)
                    break
                last_height = new_height
        trump_df = pd.DataFrame(columns=['id', 'message'])
        number = 1
        for i in range(len(total_tweets)):
            for j in range(len(total_tweets[i])):
                trump_df = trump_df.append({'id': number, 'message': (total_tweets[i][j]).text},
                                           ignore_index=True)
                number = number + 1
        print(trump_df.head())






