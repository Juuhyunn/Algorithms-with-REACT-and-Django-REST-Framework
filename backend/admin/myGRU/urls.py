from django.conf.urls import url

from admin.myGRU import views

urlpatterns = {
    url(r'process', views.process),

}