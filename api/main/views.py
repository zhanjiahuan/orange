import logging
from rest_framework.views import APIView
from django.shortcuts import render

from api.main.models import GoodsCategory, Goods,GoodsType
from api.main.main_serializers import *
from api.common.result import ResultResponse


def main(request):
    cate_list = GoodsCategory.objects.all()
    for cate in cate_list:
        sub_list = cate.goodssubcategory_set.all()
        for sub in sub_list:
            sub.type_list = sub.goodstype_set.all()
        cate.sub_list = sub_list
    return render(request, 'main.html', locals())


# 分类三级联动json
class CateView(APIView):

    def get(self, request):
        cate_list = GoodsCategory.objects.all()
        try:
            serializer = CategorySerializer(cate_list, many=True)
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()


#  商品分类级json
class GoodsSubView(APIView):

    def get(self, request):
        goods_list = GoodsSubcategory.objects.all()
        try:
            serializer = SubsSerializer(goods_list, many=True)
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()


#  商品分类级json
class GoodsView(APIView):

    def get(self, request):
        goods_list = Goods.objects.all()
        try:
            serializer = GoodsSerializer(goods_list, many=True)
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()


