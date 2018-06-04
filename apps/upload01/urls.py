from django.conf.urls import url

from apps.upload01 import views

# http://127.0.0.1:8000/media + user/homebg.png
# 二进制数据
urlpatterns = [
    url('up_img/', views.upload, name='upload'),
    url('ajax/', views.ajax_upload),
    url('register/', views.RegisterView.as_view()),

]
