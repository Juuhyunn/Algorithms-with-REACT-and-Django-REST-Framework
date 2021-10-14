from django.conf.urls import url

from admin.crime import views

urlpatterns = {
    url(r'crime-model', views.crimes),
    url(r'cctv-model', views.cctvs),
    url(r'population-model', views.populations),
    url(r'merge-cctv-population', views.merge_cctv_pop),
    url(r'merge-crime-cctv', views.merge_crime_cctv),
    url(r'process', views.process),
}
