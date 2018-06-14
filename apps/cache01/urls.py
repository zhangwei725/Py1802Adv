from django.conf.urls import url

# http://127.0.0.1:8000/media + user/homebg.png
# 二进制数据
from apps.cache01 import views

urlpatterns = [
    url('1/', views.test_cache),
    url('2/', views.test_cache1),
]
