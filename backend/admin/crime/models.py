from django.db import models
# 모델은 정형화 되어 있는 샘플 데이터(진짜 데이터) 를 가지고 있는 데이터프레임
# 데이터를 가지고 있지 않는 데이터 프레임은 데이터 스트럭쳐?
# Create your models here.
from icecream import ic

from admin.common.models import DFrameGenerator, Printer, Reader


class CrimeCctvMode(object):
    generator = DFrameGenerator()
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
        generator = self.generator
        reader = self.reader
        printer = self.printer
        generator.context = 'admin/crime/data'
        generator.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(generator)
        ic(f'파일명 : {crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        return crime_model
