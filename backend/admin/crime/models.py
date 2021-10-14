import numpy as np
from django.db import models
# 모델은 정형화 되어 있는 샘플 데이터(진짜 데이터) 를 가지고 있는 데이터프레임
# 데이터를 가지고 있지 않는 데이터 프레임은 데이터 스트럭쳐?
# Create your models here.
from icecream import ic
import pandas as pd

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
        ic('########## 프로세스 시작 ##########')
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
        # self.crime_police(crime_df, reader, vo)
        vo.fname = 'new_data/crime_police'
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
        # population_model.columns = list # 덮어썼음
        population_df.drop([26], inplace=True)
        ic('########## cctv_population DF 생성 ##########')
        cctv_pop_df = pd.merge(cctv_df, population_df)
        cctv_pop_corr = cctv_pop_df.corr()
        ic(cctv_pop_corr)
        crime_df = crime_df.groupby('구별').sum()
        crime_df['총 범죄 수'] = crime_df.loc[:, crime_df.columns.str.contains(' 발생$', case=False, regex=True)].sum(axis=1)
        crime_df['총 검거 수'] = crime_df.loc[:, crime_df.columns.str.contains(' 검거$', case=False, regex=True)].sum(axis=1)
        crime_df['총 검거율'] = crime_df['총 검거 수'] / crime_df['총 범죄 수'] * 100
        cctv_crime_df = pd.merge(cctv_df.loc[:, ['구별', '소계']], crime_df.loc[:, '총 범죄 수':'총 검거율'], on='구별')
        cctv_crime_df.rename(columns={"소계": "CCTV총합"}, inplace=True)
        ic(cctv_crime_df.corr())
        ic('############### POLICE DF 생성 ###############')
        police_df = pd.pivot_table(crime_df, index='구별', aggfunc=np.sum)
        # ic(police_df)


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


