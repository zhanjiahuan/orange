from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password

from django.core.cache import cache
from django.core.mail import send_mail
from django.views.decorators.csrf import ensure_csrf_cookie
from django_ajax.decorators import ajax
from django.template import loader
from itsdangerous import URLSafeSerializer

from api.main.models import User, Coupon
from orange import settings


def login_views(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        result = {'status': 200, }
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            if user.is_active:
                # 已激活的账户
                user = authenticate(username=username, password=password)
                if user:
                    # # 在缓存中保存session
                    # session_s = URLSafeSerializer(settings.SECRET_KEY, "session")
                    # token = session_s.dumps({'username': user.id})
                    # cache.set(token, user.id, timeout=10 * 60)
                    # # 返回json数据中携带token
                    # result.update(session_id=token)
                    login(request,user)
                    result.update(url='http://localhost:63343/orange_html/person/index.html')
                    return JsonResponse(result)

                else:
                    # 密码错误
                    result.update(status=404, msg='密码错误')
                    return JsonResponse(result)
            else:
                # 用户未激活
                result.update(status=404, msg='用户未激活')
                return JsonResponse(result)

        else:
            # 用户不存在
            result.update(status=404, msg='用户不存在')
            return JsonResponse(result)


def resgister_views(request):
    if request.method == 'GET':

        return render(request, 'register.html')
    if request.method == "POST":
        result = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_again = request.POST.get('passwordRepeat')
        if email and password and password_again:
            user = User.objects.filter(email=email)
            if user:
                result.update(user_error='账号已存在，注册失败')
                return JsonResponse(result)
            else:
                # 账号不存在
                if password == password_again:
                    new_user = User.objects.create_user(email=email, password=password, username=email, is_vip=0,
                                                        is_delete=0, is_active=0, status=1, balance=0.00, points=0)
                    if new_user:
                        # 去邮箱激活
                        auth_s = URLSafeSerializer(settings.SECRET_KEY, "auth")
                        token = auth_s.dumps({'username': new_user.username})
                        cache.set(token, new_user.id, timeout=10 * 60)
                        active_url = f'http://127.0.0.1:8000/account/active/?token={token}'
                        content = loader.render_to_string('mail.html',
                                                          request=request,
                                                          context={'username': email, 'active_url': active_url})
                        send_active_mail(subject='激活网站', content=content, to=[email])
                        # 邮件发送成功
                        result.update(mail_url='http://127.0.0.1:8000/account/checkemail/')
                        return JsonResponse(result)
                else:
                    result.update(password_error='前后密码不一致，注册失败')
                    return JsonResponse(result)
        else:
            result.update(msg='数据未获取到')
            return JsonResponse(result)


def active_account(request):
    token = request.GET.get('token')
    uid = cache.get(token)
    if uid:
        User.objects.filter(id=uid).update(is_active=1)
        return HttpResponse("激活成功")
    else:
        # 激活已经失效
        # 输入邮箱或者用户名     通过用户或者邮箱查询User对象
        # return redirect('/')
        pass


def send_active_mail(subject='', content=None, to=None):
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )


def check_eamil(request):
    return render(request, 'check_eamil.html')
