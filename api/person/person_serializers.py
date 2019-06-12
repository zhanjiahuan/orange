from rest_framework import serializers
from api.main.models import User, Order, Coupon, Collection, Goods



class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('goods',)

class CouponSerializer(serializers.ModelSerializer):
    # count = serializers.SerializerMethodField('get_coupon_count')

    class Meta:
        model = Coupon
        fields = ('value','invalid_date')

    # def get_coupon_count(self,user):
    #     return Coupon.objects.filter(user_id=user.id).count()




class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('goods_count','create_date')




class UserSerializer(serializers.ModelSerializer):
    # 外键的related_name
    user_coupons = CouponSerializer(many=True)
    user_orders = OrderSerializer(many=True)
    user_collections = CollectionSerializer(many=True)

    class Meta:
        model = User
        fields = ('email','balance','points','is_vip','user_coupons','user_orders','user_collections')


class UserInforSerialize(serializers.ModelSerializer):
    class Meta:
        model=User
        fileds=('username','realname','is_vip','sex','birthday','email','phone')


