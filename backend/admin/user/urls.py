from django.conf.urls import url

from admin.user import views
#
# urlpatterns = {
#     url(r'^api/users/register', views.users),
#     url(r'^api/users/list', views.users)
# }
urlpatterns = {
    url(r'', views.register, name='register'),
    # url(r'list', views.list),
    url(r'login', views.login)
}