from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^ngapp/', views.index, name='index'),

    # TODO: need to install django rest api instead
    url(r'^api/auth/register', views.register, name='register'),
    # url(r'^api/auth/login', views.login, name='login'),
    url(r'^api/users/me', views.me, name='me'),

]
