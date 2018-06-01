import datetime
import json

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from apps.upload01.models import Account


class UploadView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass


"""

with open('文件名','w',encoding='utf-8') as f
# file对象
  f.write()
  f.writelines()
  f.flush()
操作模式   
r 表示只读
w 表示只写  (当文件存在的时候清空内容,不存在 就创建文件)
a  追加模式  (如果文件不存在 就创建,如果文件存在就追加末尾)
+ 
b 二进制数据

"""


def upload(request):
    if request.method == 'GET':
        return render(request, 'templates/file_upload.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        # UploadFile
        upload_file = request.FILES.get('head')
        # 获取文件的名称
        #  31231.1.11.png
        # print(file_name.split('.')[-1])
        # 获取文件的大小
        # uplaod_file.size
        # 读取客服端上传整个文件数据,文件过大慎用
        # upload_file.read()
        # 把文件对象按着指定大小切割
        # chunk_size 手动指定切割文件大小
        #  返回的是一个生成器对象 10  10 * m
        """
        1.文件名不能写死,还要对图片的名字重命名
        """
        chunks = upload_file.chunks()  #
        path = get_file_path(1) + get_file_name(upload_file.name)
        with open(path, 'wb') as f:
            for chunk in chunks:
                f.write(chunk)
            f.flush()
        return HttpResponse(path, content_type='application/json')
    else:
        return HttpResponse('不支持的请求')


@csrf_exempt
def ajax_upload(request):
    result = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        path = save_file(request)
        result.update(img=path)
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        return HttpResponse('不支持的请求')


'''
文件的后缀名 

'''

"""
对图片文件进行重命名
"""


def get_file_name(old_name):
    # .png .jpg
    # 获取客服端图片的后缀名
    suffix_name = '.' + old_name.split('.')[-1]
    # 把时间类型转化指定格式的字符串输出
    # IMG20180503161930
    new_name = 'IMG%s' % (datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    return new_name + suffix_name


def save_file(request):
    upload_file = request.FILES.get('head')
    chunks = upload_file.chunks()  #
    path = get_file_path(1) + get_file_name(upload_file.name)
    with open(path, 'wb') as f:
        for chunk in chunks:
            f.write(chunk)
        f.flush()
    return path


def get_file_path(uid):
    # media/img/user/10/2018/05/31
    import os
    save_path = 'media/%s/%s/%s/%s/%s/' % ('img/user', uid,
                                           datetime.datetime.now().year,
                                           datetime.datetime.now().month,
                                           datetime.datetime.now().day)
    # 如果文件路径不存在
    if not os.path.exists(save_path):
        # 就创建目录
        os.makedirs(save_path)
    return save_path


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    """
        # python 自带的md5加密
        import hashlib
        md5 = hashlib.md5
       
        password = md5.update(password.encode(encoding='utf-8'))
        # django字典的加密方式
        encrypt_password = make_password(password)
    """

    @csrf_exempt
    def post(self, request):
        # 对密码进行加密
        email = request.POST.get('email')
        # 对密码进行加密
        encrypt_password = make_password(request.POST.get('password'))
        contact = request.POST.get('contact')
        company = request.POST.get('company')
        tel = request.POST.get('tel')
        qq = request.POST.get('qq')
        head = save_file(request)
        try:
            Account.objects.get(email=email)
        except Account.DoesNotExist:
            Account.objects.create(email=email,
                                   password=encrypt_password,
                                   company=company,
                                   contacts=contact,
                                   phone=tel,
                                   qq=qq,
                                   head=head
                                   )
        return render(request, 'index.html')
