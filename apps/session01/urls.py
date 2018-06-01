from django.conf.urls import url

from apps.session01 import views

urlpatterns = [
    url('cookie/', views.test_cookie),
    url('test02/', views.test02),
]
