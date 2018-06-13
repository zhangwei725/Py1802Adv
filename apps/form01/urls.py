from django.conf.urls import url

from apps.form01 import views
#
urlpatterns = [
    url('1/', views.login),
    url('2/', views.register),
]
