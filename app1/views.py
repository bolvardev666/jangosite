from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as dj_login

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# Create your views here.
def index(request):
    pass


def login(request):
    say_alter = {'go': True}
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            logging.debug("登录form验证成功!\t用户名:{0}\t密码:{1}".format(username, password))
            user = authenticate(username=username, password=password)
            if user.is_active:
                dj_login(request, user)
                logging.debug("账户已启用")
                request.session.set_expiry(0)
                return redirect("/index")
            else:
                logging.debug("账户未启用,发送弹窗")
                return render(request, "login.html", {"form": form, "say_alter": say_alter})
        else:
            logging.debug("登录form验证失败")
            logging.debug("正在进入GET请求视图")
    return render(request, "login.html", {"form": form})
