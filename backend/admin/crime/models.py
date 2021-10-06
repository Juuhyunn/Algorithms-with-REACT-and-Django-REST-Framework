from django.db import models
# 모델은 정형화 되어 있는 샘플 데이터(진짜 데이터) 를 가지고 있는 데이터프레임
# 데이터를 가지고 있지 않는 데이터 프레임은 데이터 스트럭쳐?
# Create your models here.
from admin.common.models import DFrameGenerator, Printer, Reader


class CrimeCctvMode():
    def __init__(self):
        self.dfg = DFrameGenerator()
        self.printer = Printer()
        self.reader = Reader()
    