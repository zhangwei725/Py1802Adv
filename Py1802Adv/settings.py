import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '2^tk958+@md))-t$5#an7nq2eyt2^67pfxa4k37*hcf7jl=ss#'

DEBUG = True

ALLOWED_HOSTS = []

MY_APP = [
    'apps.upload01',
    'apps.session01',
    'apps.form01',
    'apps.cache01',
]
SYS_APP = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = SYS_APP + MY_APP

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]
#
# CACHE_MIDDLEWARE_SECONDS = 60 * 60

ROOT_URLCONF = 'Py1802Adv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Py1802Adv.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'adv',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
# 配置静态文件
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 上传目录
MEDIA_ROOT = BASE_DIR + '/media/'
MEDIA_URL = '/media/'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024

# 跟session配置相关

# 配置cookie存储的键 sessionid=
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_AGE = 7 * 24 * 60 * 60  # session cookie的失效时间
# 是否关闭浏览器session失效
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# True  如果30分钟没有跟服务器进行通信 session就会失效
SESSION_SAVE_EVERY_REQUEST = True
# 配置session存储方式
# SESSION_ENGINE = 'django.contrib.session.backends.db'
# 使用内存缓存
# SESSION_ENGINE = 'django.contrib.session.backends.cache'

# 使用文件缓存
# SESSION_ENGINE = 'django.contrib.session.backends.file'
# 指定文件缓存的目录
# SESSION_FILE_PATH = ""
# var/folders/d3/xxfsdfsfdsfdsfds
# 采用内存缓存 + 数据库
# SESSION_ENGINE = 'django.contrib.session.backends.cache_db'

"""===========缓存配置start============"""
CACHE = {
    # 'default': {
    #     #  指定缓存方式 (文件缓存)
    #     'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #     # 指定缓存文件的保存路径
    #     'LOCATION': 'file://d:/cache/tmall',  # 可选
    #     """
    #     缓存有效期
    #     正整数  默认300秒
    #     None 永不过期
    #     0 立即过期
    #     """
    #     'TIMEOUT': 500
    # },
    # 小网站 ,例如内部使用的系统

    #     必须先安装 Memcache数据库
    #     下载python-memcache库
    # 'default': {
    #     #  指定缓存方式 (Memcache)
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     # 指定缓存数据库的ip地址和端口python-memcache
    #     'LOCATION': '127.0.0.1:11211',
    #     'TIMEOUT': 500
    # },

    # 需要依赖 pylibmc
    # 'default': {
    #     #  指定缓存方式 (Memcache)
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     # 指定缓存数据库的ip地址和端口python-memcache
    #     'LOCATION': '127.0.0.1:11211',
    #     'TIMEOUT': 500
    # }
    #     使用redis缓存
    #    安装第三方的库  django-redis

    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # 指定缓存数据库的ip地址和端口python-memcache
        'LOCATION': 'redis://127.0.0.1:6379',
        'TIMEOUT': 500
    }
}
# 文件   数据库   缓存+ 数据   redis
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
