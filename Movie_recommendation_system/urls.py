"""Movie_recommendation_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# 主路由，匹配前面部分
from django.contrib import admin
from django.urls import path, include  # 要进行分布式路由的配置，引入include
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),  # 没咋用到admin，可以注释掉
    path('', views.IndexView.as_view(), name='index'),
    path('movie/', include('movie.urls')),  # 本来这个参数是视图函数，是交给视图函数来处理的
    # 现在要交给应用的urls，让它去分发给自己的views
]
