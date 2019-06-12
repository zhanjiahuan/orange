import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_ajax.decorators import ajax
# from pip._internal.utils import logging
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from api.common.result import ResultResponse
from api.main.models import User
from api.person.person_serializers import UserSerializer, UserInforSerialize


@api_view(['GET'])
def api_user_center(request):
    '''
    个人中心首页接口,返回username,会员等级,优惠券数量,账户余额,总积分,订单内容,收藏
    :param request:
    :return:
    '''
    user = User.objects.filter(id=5)
    if user.exists():
        try:
            serializer = UserSerializer(user, many=True)
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()


@api_view(['GET', 'POST'])
def api_user_info(request):
    '''
    get,post两种请求,get请求读取 username,会员等级,realname,性别,生日,电话,邮箱
    post请求,接收json数据,做修改操作
    :param request:
    :return:
    '''
    if request.method=='GET':
        user = User.objects.filter(id=5)
        try:
            serializer = UserInforSerialize(user, many=True)
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()


class ApiUserSafe(APIView):
    def get(self, request):
        '''
        做读取数据操作
        :param request:
        :return:
        '''

    def post(self, request):
        '''
        做修改操作
        :param request:
        :return:
        '''
