from django.conf.urls import url

from admin.myLSTM import views

urlpatterns = {
    url(r'process', views.process),

}