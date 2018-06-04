from django.contrib.sessions.backends.cache import SessionStore
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# cookie 存储数据的格式  key:value
"""
如何获取cookie信息 -----> 通过request对象获取
如何设置 HttpResponse-----> 设置cookie信息
说明一下
当用户第一次访问网站的时候 获取不到任何cookie信息
拿响应的时候可以设置一些cookie信息
下次来的时候浏览器会自动把cookie信息传入服务器,拿服务器就可以通过 
request.COOKIE.get(key)拿到相关的数据

"""
"""
set_cookie

参数说明 
key  键
value 值
max_age  cookie信息过期的时间 多久过期
expires =  过期时间 具体的某个时间点 主要不要用 max_age同时使用
path='/' cookie生效的路径  默认所有的连接都能获取cookie信息
domain   cooke生效的域名
httponly=False   默认为True  如果是False只能http协议传输 js无法获取cookie 
"""


# session
def test_cookie(request):
    resp = HttpResponse('测试cookie')
    msg = request.COOKIES.get('msg')
    print(msg)
    if not msg:
        resp.set_cookie('msg', 'hello', path='/sc/cookie/')
    return resp


def test_signed_cookie(request):
    resp = HttpResponse('测试cookie')
    msg = request.get_signed_cookie('num', salt='afsfsdfs')
    print(msg)
    if not msg:
        # resp.set_cookie('msg', 'hello', path='/sc/cookie/')
        resp.set_signed_cookie('num', 1, alt='afsfsdfs')

    return resp


def test02(request):
    resp = HttpResponse('测试cookie')
    msg = request.COOKIES.get('msg')
    print(msg)
    return resp


def session01(request):
    # SessionStore()
    session_store = request.session
    # 不存在就设置,存在就覆盖
    session_store['s1'] = 123
    # 存在就不设置,不存在就设置
    session_store.setdefault('s2', '111111')
    return HttpResponse('session, test01')


def session02(request):
    # SessionStore()
    session_store = request.session
    s1 = session_store['s1']  # 当key不存在就出异常
    # 获取值
    s1 = session_store.get('s2')
    print(s1)
    # 获取当前session所有的键
    keys = session_store.keys()
    # 获取所有的值
    values = session_store.values()
    for value in values:
        print(value)
    # 获取所有的键值对
    items = session_store.items()
    for key, value in items:
        print(key)
        print(value)
        # session_id
        # session_id = session_store.session_key
        # # 005ethyda0ltv46nbxa4fzkuq652cy2v
        # c = request.COOKIES.get("sessionid")
        # print(session_id)

        #    删除

    # session_store.pop()

    return HttpResponse('session, 获取session')


def del_session(request):
    session_store = request.session
    # 判断key是否存在,存在就是True
    if session_store.exists('s1'):
        del session_store['s1']
    print('删除成功')
    return HttpResponse('session,删除session')


def set_exp(request):
    session_store = request.session
    """
    设置session过期时间
    参数说明  
    value
    1> 如果value是一个正整数 session会在设置的秒数后失效
    2> datetime  session 会在指定的时间失效
    3> 0   用于关闭浏览器失效 
    4> None  默认 依赖全局
    """
    session_store.set_expiry(0)
    session_store.setdefault('expiry', 'test')
    return HttpResponse('session,局部设置过期时间')


# 测试重定向技术
def test_redirect(request):
    return redirect('/session/5/')


def test(request):
    session_store = request.session
    expiry = session_store.get('expiry')
    return HttpResponse('session,删除session')


# 7天免登陆
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'xiaoming' and password == '123':
            request.session['user'] = {'username': 'xiaming', 'uid': 1}
            return redirect('/session/index/')
    else:
        return render(request, 'login.html')


#     cookie 4k   只能存asc||

def index(request):
    user = request.session.get('user')
    return render(request, 'index.html', {'user': user})


def register(request):
    return None


def loginout(request):
    del request.session['user']
    return redirect('/session/index')






