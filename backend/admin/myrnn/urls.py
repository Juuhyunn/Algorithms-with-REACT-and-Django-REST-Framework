from django.conf.urls import url

from admin.myrnn import views

urlpatterns = {
    url(r'ram_price', views.ram_price),
    url(r'kia_predict', views.kia_predict),

}