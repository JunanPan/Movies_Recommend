from django.http import request
from django.shortcuts import render,redirect,reverse
# 直接使用render加载并相应模板，简化代码过程，以前使用loader


def index(request):
    return render(request,'index.html')
