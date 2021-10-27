import matplotlib.pyplot as plt
import numpy as np
from icecream import ic
import pandas as pd
from sklearn import preprocessing
from wordcloud import WordCloud

from admin.common.models import ValueObject, Printer, Reader
import csv
import datetime as dt
from bs4 import BeautifulSoup
from selenium import webdriver
from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import re

# !pip install git+https://git@github.com/kavgan/word_cloud.git
# !apt-get update
# !apt-get install g++ openjdk-8-jdk python-dev python3-dev
# !pip3 install JPype1-py3
# !pip3 install konlpy
# !JAVA_HOME="C:\Program Files\Java\jdk1.8.0_241"
class NewsCrawling(object):
    # 멤버변수(1) - 브라우저 버전 정보 문자열
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

    # 멤버변수(2) - 접속에 사용될 세션객체 (생성자에서 사용된다.)
    session = None

    # -----------------------------------------------------
    # 생성자 - 접속 세션을 생성한다.
    # -----------------------------------------------------
    def __init__(self, referer=''):
        ses_info = {'referer': referer, 'User-agent': self.user_agent}
        # 세션객체 생성
        self.session = requests.Session()
        # 세션에 접속 정보 설정
        self.session.headers.update(ses_info)

    # -----------------------------------------------------
    # HTML 페이지에 접속하여 페이지의 모든 소스코드를 가져온다.
    # -----------------------------------------------------
    def get(self, url, encoding='utf-8'):
        # 생성자에서 만든 세션 객체를 사용하여 URL에 접근
        r = self.session.get(url)

        # 에러가 발생했다면 None을 리턴하고 처리 중단
        if r.status_code != 200:
            return None

        # 인코딩 설정
        r.encoding = encoding

        # 결과 문자열의 앞,뒤 공백을 제거한 상태로 리턴
        return r.text.strip()

    # -----------------------------------------------------
    # HTML 페이지에 접속하여 특정 셀렉터에 대하여 파싱한 결과를 List로 반환한다.
    # -----------------------------------------------------
    def select(self, url, selector='html', encoding='utf-8'):
        # 웹 페이지 접속 함수를 호출하여 소스코드 리턴받기
        source = self.get(url, encoding)

        # 리턴값이 없다면 처리 중단
        if not source:
            return None

        # 웹 페이지의 소스코드 HTML 분석 객체로 생성
        soup = BeautifulSoup(source, 'html.parser')

        # CSS 선택자를 활용하여 가져오기를 원하는 부분 지정
        # -> list로 리턴
        return soup.select(selector)

    # -----------------------------------------------------
    # 크롤링한 결과 원본(item)에서 tag와 selector가 일치하는 항목을 삭제
    # -----------------------------------------------------
    def remove(self, item, tag, selector=None):
        for target in item.find_all(tag, selector):
            target.extract()

    # -----------------------------------------------------
    # 특정 URL의 파일을 다운로드 한다.
    # -----------------------------------------------------
    def download(self, url, filename=""):
        # 접속 객체를 사용하여 파라미터로 전달된 URL 다운로드 받기
        r = self.session.get(url, stream=True)

        # 에러여부 검사 - 에러가 발생했다면 None을 리턴하며 처리 종료
        if r.status_code != 200:
            return None

        # 이미지의 byte 데이터를 추출
        img = r.raw.read()

        # 추출한 데이터를 저장
        with open(filename, 'wb') as f:
            f.write(img)

        # 저장된 파일 이름만 리턴
        return filename


# 크롤링 클래스에 대한 객체를 생성
# -> 이 파일을 모듈로서 참조하는 다른 파일이 사용할 수 있다.
# crawler = Crawler()


class Crawling(object):
    def __init__(self):
        pass

    def process(self):
        # nltk.download()
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        # self.naver_movie()
        # self.tweet_trump()
        self.samsung_report(vo)

    def samsung_report(self, vo):
        # okt = Okt()
        okt = Okt()
        daddy = okt.pos('아버지 가방에 들어가신다', norm=True, stem=True)
        print(f':::: {dt.datetime.now()} ::::::\n {daddy} ')
        okt.pos('삼성전자 글로벌센터 전자사업부', stem=True)
        with open(f'{vo.context}kr-Report_2018.txt', 'r',
                  encoding='UTF-8') as f:
            texts = f.read()
        # print(texts)
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        temp = tokenizer.sub('', temp)
        tokens = word_tokenize(temp)
        noun_tokens = []
        for i in tokens:
            token_pos = okt.pos(i)
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(temp)) > 1:
                noun_tokens.append(''.join(temp))
        noun_tokens_join  = ' '.join(noun_tokens)
        tokens = word_tokenize(noun_tokens_join)
        # print(texts)
        with open(f'{vo.context}stopwords.txt', 'r', encoding='UTF-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
        texts_without_stopwords = [text for text in tokens if text not in stopwords]
        # print(f':::::::: {datetime.now()} ::::::::\n {texts_without_stopwords[:10]}')
        freq_texts = pd.Series(dict(FreqDist(texts_without_stopwords))).sort_values(ascending=False)
        # print(f':::::::: {datetime.now()} ::::::::\n {freq_texts[:30]}')
        wcloud = WordCloud(f'{vo.context}D2Coding.ttf', relative_scaling=0.2,
                           background_color='white').generate(' '.join(texts_without_stopwords))
        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(f'{vo.context}wcloud.png')
        print(f':::::::: {dt.datetime.now()} :::::::')


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






