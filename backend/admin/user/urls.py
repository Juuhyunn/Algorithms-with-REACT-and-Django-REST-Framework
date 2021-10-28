from django.conf.urls import url

from admin.user import views
#
# urlpatterns = {
#     url(r'^api/users/register', views.users),
#     url(r'^api/users/list', views.users)
# }
urlpatterns = {
    url(r'', views.users, name='register'),
    url(r'', views.users, name='list'),
    # url(r'login', views.users),
    # url(r'<slug:id>', views.users),
}