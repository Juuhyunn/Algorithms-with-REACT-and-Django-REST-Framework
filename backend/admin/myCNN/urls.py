from django.conf.urls import url

from admin.myCNN import views

urlpatterns = {
    url(r'catdog', views.CatDogClassification),
    url(r'cifa', views.cifa_process),

}