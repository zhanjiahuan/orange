# 工具类 : 对返回结果信息的封装
from django.http import JsonResponse
# 导入http状态码
from rest_framework import status
# 成功返回json消息
SUCCESS_MSG = 'success'
FAILD_MSG = 'not found'


class ResultResponser:
    @staticmethod
    def success_response(data,status=status.HTTP_200_OK,msg=SUCCESS_MSG):
        res = {'status':status,'msg':msg,'date':data}
        return JsonResponse(res)

    @staticmethod
    def faild_response(status=status.HTTP_404_NOT_FOUND,msg=FAILD_MSG):
        res = {'status': status, 'msg': msg}
        return JsonResponse(res)
