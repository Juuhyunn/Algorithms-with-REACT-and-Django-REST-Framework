from django.conf.urls import url

from admin.user import views
#
# urlpatterns = {
#     url(r'^api/users/register', views.users),
#     url(r'^api/users/list', views.users)
# }
urlpatterns = {
    url(r'register', views.users),
    url(r'list', views.users)
}