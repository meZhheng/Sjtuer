"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # path(route, views, name=None)
    # route:字符串类型，匹配请求路径
    # 指定路径所对应的视图函数的名称
    # 为地址起别名

    # path('route/<转换器类型：自定义名>， views.xxx'
    # 注：此时views函数要增加一个参数，该参数为自定义名
    # 转换器类型有：str（匹配除'/'之外的非空字符串), int（匹配0或任何正整数,且保证返回int）
    #             slug(匹配任意由字母,数字,连字符,下划线组成的短标签）
    #             path(匹配非空字符串，包括'/')

    # 限制转换器匹配的范围,正则表达式，且为命名分组模式
    # re_path(reg, view, name = xxx)

    path('admin/', admin.site.urls),
    path('', views.login_view),
    re_path(r'^page/(?P<pg>\d{1,2})$', views.page_valid_view),
    path('page/<int:pg>/', views.page_invalid_view),
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$', views.cal2_view),
    path('<int:m>/<str:op>/<int:n>', views.cal1_view),
    path('request', views.request_study_view),
    path('test_get_post', views.test_getmethod),
    path('test_html', views.test_html),

    path('bookstore/', include('bookstore.urls')),
    path('index', views.index_view),
]
