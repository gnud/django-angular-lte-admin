from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ngapp/', views.index, name='index')
]
