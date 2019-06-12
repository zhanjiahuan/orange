from rest_framework import serializers
from api.main.models import *


class GoodsParamValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsParamValue
        fields = ('value',)


class GoodsParamSerializer(serializers.ModelSerializer):
    params = GoodsParamValueSerializer(many=True)

    class Meta:
        model = GoodsParam
        fields = ('name', 'params')


class GoodsSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsSku
        fields = ('name', 'values')


class GoodsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsDetail
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    goods_sku = GoodsSkuSerializer(many=True)
    goods_detail = GoodsDetailSerializer(many=True)
    goods_params = GoodsParamSerializer(many=True)

    class Meta:
        model = Goods
        # fields = '__all__'
        fields = ('name', 'goods_id', 'type', 'creator', 'goods_sku', 'goods_params', 'goods_detail',)


class TypesSerializer(serializers.ModelSerializer):
    types = GoodsSerializer(many=True)

    class Meta:
        model = GoodsType
        fields = ('name', 'type_id', 'status', 'types')


class SubsSerializer(serializers.ModelSerializer):
    subs = TypesSerializer(many=True)

    class Meta:
        model = GoodsSubcategory
        # fields = '__all__'
        fields = ('name', 'sub_id', 'status', 'subs')

# 三级列表


class GoodsTypeSerializer(serializers.ModelSerializer):
    # types = GoodsSerializer(many=True)

    class Meta:
        model = GoodsType
        fields = ('name', 'type_id', 'status')


class SubcategorySerializer(serializers.ModelSerializer):
    subs = GoodsTypeSerializer(many=True)

    class Meta:
        model = GoodsSubcategory
        # fields = '__all__'
        fields = ('name', 'sub_id', 'status', 'subs')


class CategorySerializer(serializers.ModelSerializer):
    cates = SubcategorySerializer(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'
