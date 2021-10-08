from django.db import models
# 모델은 정형화 되어 있는 샘플 데이터(진짜 데이터) 를 가지고 있는 데이터프레임
# 데이터를 가지고 있지 않는 데이터 프레임은 데이터 스트럭쳐?
# Create your models here.
from icecream import ic
import pandas as pd

from admin.common.models import ValueObject, Printer, Reader


class CrimeCctvMode(object):
    vo = ValueObject()
    printer = Printer()
    reader = Reader()

    def __init__(self):
        '''
        features of Raw data
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.crime_columns = ["살인 발생", "강도 발생", "강간 발생", "절도 발생", "폭력 발생"] # Nominal
        self.arrest_columns = ["살인 검거", "강도 검거", "강간 검거", "절도 검거", "폭력 검거"] # Nominal
        self.arrest_rate_columns = ["살인 검거율", "강도 검거율", "강간 검거율", "절도 검거율", "폭력 검거율"] # Ratio

    def create_crime_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
        vo.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(vo)
        ic(f'******파일명 : {crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        return crime_model

    def create_police_position(self):
        crime = self.create_crime_model()
        reader = self.reader
        station_names = []
        # for name in crime['관서명']:
        #     station_names.append(f'서울 {str(name[:-1])} 경찰서')
        [station_names.append(f'서울 {str(name[:-1])} 경찰서') for name in crime['관서명']]
        ic("*************")
        ic(station_names)
        ic("*************")
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
            ic(f'{name} : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_address:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        # crime['주현'] = gu_names
        # # 구와 경찰서의 위치가 다른 경우 수작업
        # crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        # crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        # crime.loc[crime['관서명'] == '강서서', ['구별']] = '종로구'
        # crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        # crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        # crime.loc[crime['관서명'] == '수서서', ['구별']] = '주현구'
        # crime.to_csv(self.vo.context + 'new_data/police_positions.csv')
        crime['구별'] = gu_names
        print('==================================================')
        print(f"샘플 중 혜화서 정보 : {crime[crime['관서명'] == '혜화서']}")
        print(f"샘플 중 금천서 정보 : {crime[crime['관서명'] == '금천서']}")
        crime.to_csv(self.vo.context+'new_data/police_positions.csv')
        return crime


    def create_cctv_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
        vo.fname = 'CCTV_in_Seoul'
        cctv_file_name = reader.new_file(vo)
        ic(f'******파일명 : {cctv_file_name}')
        cctv_model = reader.csv(cctv_file_name)
        printer.dframe(cctv_model)
        cctv_model.rename(columns={'기관명':'구별'}, inplace=True)
        ic('********************')
        printer.dframe(cctv_model)
        cctv_model.to_csv(self.vo.context+'new_data/cctv_positions.csv')
        return cctv_model

    def create_population_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
        vo.fname = 'population_in_Seoul'
        population_file_name = reader.new_file(vo)
        ic(f'******파일명 : {population_file_name}')
        population_model = reader.xls(population_file_name, 2, ('B, D, G, J, N'))
        list = ['구별', '인구수', '한국인', '외국인', '고령자']
        population_model.rename(columns={population_model.columns[i]: list[i] for i in range(len(list))}, inplace=True) #일부만 변경할 수 있음
        # population_model.columns = list # 덮어썼음
        population_model.drop([26], inplace=True)
        printer.dframe(population_model)
        population_model.to_csv(self.vo.context+'new_data/population_positions.csv')
        return population_model

    def merge_cctv_population(self):
        cctv = self.create_cctv_model()
        pop = self.create_population_model()
        merge = pd.merge(cctv, pop)
        '''
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        '''
        ic(merge.corr())
        '''
                           소계    2013년도 이전   2014년    2015년   2016년     인구수     한국인     외국인     고령자
          소계           1.000000   0.862756  0.450062  0.624402  0.593398  0.306342  0.304287 -0.023786  0.255196
          2013년도 이전   0.862756   1.000000  0.121888  0.257748  0.355482  0.168177  0.163142  0.048973  0.105379
          2014년         0.450062   0.121888  1.000000  0.312842  0.415387  0.027040  0.025005  0.027325  0.010233
          2015년         0.624402   0.257748  0.312842  1.000000  0.513767  0.368912  0.363796  0.013301  0.372789
          2016년         0.593398   0.355482  0.415387  0.513767  1.000000  0.144959  0.145966 -0.042688  0.065784
          인구수          0.306342   0.168177  0.027040  0.368912  0.144959  1.000000  0.998061 -0.153371  0.932667
          한국인          0.304287   0.163142  0.025005  0.363796  0.145966  0.998061  1.000000 -0.214576  0.931636
          외국인         -0.023786   0.048973  0.027325  0.013301 -0.042688 -0.153371 -0.214576  1.000000 -0.155381
          고령자          0.255196   0.105379  0.010233  0.372789  0.065784  0.932667  0.931636 -0.155381  1.000000

        '''
        self.printer.dframe(merge)
        merge.to_csv(self.vo.context+'new_data/merge_cctv_population.csv')
        return merge

    def merge_crime_cctv(self):
        crime_model = self.reader.csv('admin/crime/data/new_data/police_positions')
        crime = crime_model[self.crime_columns]
        arrest = crime_model[self.arrest_columns]
        gu = crime_model["구별"]
        crime_ls = []
        arrest_ls = []
        [crime_ls.append(sum([int(j) for j in crime.loc[i]])) for i in range(len(crime.index))]
        [arrest_ls.append(sum([int(j) for j in arrest.loc[i]])) for i in range(len(arrest.index))]
        crime['발생'] = crime_ls
        arrest['검거'] = arrest_ls
        result = pd.concat([gu, crime['발생'], arrest['검거']], axis=1)

        grouped = result.groupby('구별')
        crime_filter = grouped['발생', '검거'].sum()
        crime_filter.to_csv('admin/crime/data/new_data/test.csv')