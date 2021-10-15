import csv
from datetime import datetime

import numpy as np
from django.db import models
# 모델은 정형화 되어 있는 샘플 데이터(진짜 데이터) 를 가지고 있는 데이터프레임
# 데이터를 가지고 있지 않는 데이터 프레임은 데이터 스트럭쳐?
# Create your models here.
from icecream import ic
import pandas as pd
from sklearn import preprocessing

from admin.common.models import ValueObject, Printer, Reader


class Crime(object):
    def __init__(self):
        pass
        '''
        features of Raw data
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
    # noinspection PyMethodMayBeStatic
    def process(self):
        ic(f'########## 프로세스 시작 - {datetime.now()} ##########')
        vo = ValueObject()
        printer = Printer()
        reader = Reader()
        vo.context = 'admin/crime/data/'
        crime_columns = ["살인 발생", "강도 발생", "강간 발생", "절도 발생", "폭력 발생"] # Nominal
        arrest_columns = ["살인 검거", "강도 검거", "강간 검거", "절도 검거", "폭력 검거"] # Nominal
        arrest_rate_columns = ["살인 검거율", "강도 검거율", "강간 검거율", "절도 검거율", "폭력 검거율"] # Ratio
        ic('########## crime DF 생성 ##########')
        vo.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(vo)
        crime_df = reader.csv(crime_file_name)
        ic('########## police station DF 생성 ##########')
        self.police_staion(crime_df, reader, vo)
        vo.fname = 'new_data/police_positions'
        crime_df = reader.csv(reader.new_file(vo))
        ic('########## cctv DF 생성 ##########')
        vo.fname = 'CCTV_in_Seoul'
        cctv_df = reader.csv(reader.new_file(vo))
        cctv_df.rename(columns={'기관명': '구별'}, inplace=True)
        ic('########## population DF 생성 ##########')
        vo.fname = 'population_in_Seoul'
        population_df = reader.xls(reader.new_file(vo), 2, ('B, D, G, J, N'))
        list = ['구별', '인구수', '한국인', '외국인', '고령자']
        population_df.rename(columns={population_df.columns[i]: list[i] for i in range(len(list))},
                                inplace=True)  # 일부만 변경할 수 있음
        # population_df.columns = list # 덮어썼음
        population_df.drop([26], inplace=True)
        ic('########## cctv_population DF MERGE 생성 ##########')
        cctv_pop_df = pd.merge(cctv_df, population_df)
        cctv_pop_corr = cctv_pop_df.corr()
        ic(cctv_pop_corr)
        '''
            CCTV와 상관계수: 한국인 0.3, 외국인 0, 고령자 0.2   
        '''
        crime_df = crime_df.groupby('구별').sum()
        crime_df['총 범죄 수'] = crime_df.loc[:, crime_df.columns.str.contains(' 발생$', case=False, regex=True)].sum(axis=1)
        crime_df['총 검거 수'] = crime_df.loc[:, crime_df.columns.str.contains(' 검거$', case=False, regex=True)].sum(axis=1)
        crime_df['총 검거율'] = crime_df['총 검거 수'] / crime_df['총 범죄 수'] * 100
        cctv_crime_df = pd.merge(cctv_df.loc[:, ['구별', '소계']], crime_df.loc[:, '총 범죄 수':'총 검거율'], on='구별')
        cctv_crime_df.rename(columns={"소계": "CCTV총합"}, inplace=True)
        ic(cctv_crime_df.corr())
        '''
        CCTV와 상관계수: 범죄수 0.47, 검거수 0.52 
        '''
        ic('############### POLICE DF 생성 ###############')
        police_df = pd.pivot_table(crime_df, index='구별', aggfunc=np.sum)
        ic(police_df)
        ic(f'police df 컬럼 : {police_df.columns}')
        '''
        "police df 컬럼 : Index(['Unnamed: 0', '강간 검거', '강간 발생', '강도 검거', '강도 발생', '살인 검거', '살인 발생',
                                           '절도 검거', '절도 발생', '총 검거 수', '총 검거율', '총 범죄 수', '폭력 검거', '폭력 발생'], dtype='object') "
        '''

        # police_df['살인 검거율'] = (police_df['살인 검거'].astype(int) / police_df['살인 발생'].astype(int)) * 100
        # police_df['강도 검거율'] = (police_df['강도 검거'].astype(int) / police_df['강도 발생'].astype(int)) * 100
        # police_df['강간 검거율'] = (police_df['강간 검거'].astype(int) / police_df['강간 발생'].astype(int)) * 100
        # police_df['절도 검거율'] = (police_df['절도 검거'].astype(int) / police_df['절도 발생'].astype(int)) * 100
        # police_df['폭력 검거율'] = (police_df['폭력 검거'].astype(int) / police_df['폭력 발생'].astype(int)) * 100
        for i, j in enumerate(crime_columns):
            police_df[arrest_rate_columns[i]] = (police_df[arrest_columns[i]].astype(int) / police_df[j].astype(int)) * 100
        police_df.drop(columns=dict(zip(arrest_columns, [])), axis=1, inplace=True)

        for i in arrest_rate_columns:
            police_df.loc[police_df[i] > 100, 1] = 100  # 데이터값 기간이 1년을 넘긴 경우가 있어서 100을 max 로 지정
        police_df.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        x = police_df[arrest_rate_columns].values
        # from sklearn import preprocessing 추가
        min_max_scalar = preprocessing.MinMaxScaler()
        # 스케일링은 선형변환을 적용하여 전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        # 정규화 normalization
        # 1. 빅데이터를 처리하면서 데이터의 범위(도메인)을 일치시킨다
        # 2. 분포(스케일)을 유사하게 만든다
        police_norm_df = pd.DataFrame(x_scaled, columns=crime_columns, index=police_df.index)
        police_norm_df[arrest_rate_columns] = police_df[arrest_rate_columns]
        police_norm_df['범죄'] = np.sum(police_norm_df[crime_columns], axis=1)
        police_norm_df['검거'] = np.sum(police_norm_df[arrest_rate_columns], axis=1)
        police_norm_df.to_csv(vo.context + 'new_data/police_norm.csv')



    def police_staion(self, crime_df, reader, vo):
        station_names = []
        [station_names.append(f'서울 {str(name[:-1])} 경찰서') for name in crime_df['관서명']]
        station_address = []
        station_lats = []
        station_lngs = []
        gmaps = reader.gmaps()
        for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_address.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_lats.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
            # ic(f'{name} : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_address:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime_df['구별'] = gu_names
        crime_df.to_csv('admin/crime/data/new_data/police_positions.csv')
        test = dict(zip(station_lats, station_lngs))
        print(test)
        with open('admin/crime/data/new_data/test_map.csv', 'w', encoding='UTF-8') as f:
            w = csv.writer(f)
            w.writerow(test.keys())
            w.writerow(test.values())
        print('완료?')


