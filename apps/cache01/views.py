from django.shortcuts import render
import datetime

# 缓存的应用
# 全局缓存 ----> 中间件
# 局部(需要配合模板技术)
# 单视图(在视图函数使用)
from django.views.decorators.cache import cache_page


def test_cache(request):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'cache.html', {'time': time})


# 单个视图函数缓存
@cache_page(5)
def test_cache1(request):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'cache_page.html', {'time': time})
