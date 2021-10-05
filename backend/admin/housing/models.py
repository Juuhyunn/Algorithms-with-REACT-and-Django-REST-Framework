from django.db import models
from icecream import ic
import pandas as pd
# from admin.common.models import Dataset


class HousingService(object):
    # dataset = Dataset()

    def new_model(self) -> object:
        return pd.read_csv(f'admin/housing/data/housing.csv')


# class Housing(models.Model):
#     use_in_migrations = True
#     housing_id = models.AutoField(primary_key=True)
#     longitude = models.FloatField()
#     latitude = models.FloatField()
#     housing_median_age = models.FloatField()
#     total_rooms = models.FloatField()
#     total_bedrooms = models.FloatField()
#     population = models.FloatField()
#     households = models.FloatField()
#     median_income = models.FloatField()
#     median_house_value = models.FloatField()
#     ocean_proximity = models.TextField()
#
#     class Meta:
#         db_table = 'housings'
#
#     def __str__(self):
#         return f'[{self.pk}] {self.housing_id}'


if __name__ == '__main__':
    h = HousingService()
    ic(h.new_model())