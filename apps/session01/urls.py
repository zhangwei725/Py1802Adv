from django.conf.urls import url

from apps.session01 import views

urlpatterns = [
    url('cookie/', views.test_cookie),
    url('test02/', views.test02),
    url('1/', views.session01),
    url('2/', views.session02),
    url('3/', views.del_session),
    url('4/', views.set_exp),
    url('5/', views.test),
    url('login/', views.login, name='login'),
    url('register/', views.register, name='register'),
    url('loginout/', views.loginout, name='loginout'),
    url('index/', views.index, name='index'),
    url('redirect/', views.test_redirect),

]
