from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class BankCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True,related_name='user_bankcars')
    card_num = models.CharField(max_length=30)
    card_type = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'bank_card'


class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    goods = models.ForeignKey('Goods', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True,related_name='user_collections')
    create_date = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'collection'


class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    creator = models.ForeignKey('Creator', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True,related_name='user_coupons')
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    begin_date = models.DateTimeField(blank=True, null=True)
    invalid_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'coupon'


class Creator(models.Model):
    creator_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'creator'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class Goods(models.Model):
    goods_id = models.IntegerField(primary_key=True)
    type = models.ForeignKey('GoodsType', models.DO_NOTHING,related_name='types')
    creator = models.ForeignKey('Creator', models.DO_NOTHING)
    name = models.CharField(max_length=100)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'goods'


class GoodsDetail(models.Model):
    detail_id = models.IntegerField(primary_key=True)
    goods = models.ForeignKey('Goods', models.DO_NOTHING,related_name='goods_detail')
    brand_name = models.CharField(max_length=50)
    brand_id = models.IntegerField(blank=True, null=True)
    sale_state = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    origin_price = models.DecimalField(max_digits=10, decimal_places=2)
    promote_price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    stock = models.IntegerField()
    image = models.CharField(max_length=255)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'goods_detail'


class GoodsParam(models.Model):
    param_id = models.IntegerField(primary_key=True)
    goods = models.ForeignKey('Goods', models.DO_NOTHING,related_name='goods_params')
    name = models.CharField(max_length=20)
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'goods_param'


class GoodsParamValue(models.Model):
    param_value_id = models.IntegerField(primary_key=True)
    param = models.ForeignKey('GoodsParam', models.DO_NOTHING,related_name='params')
    value = models.CharField(max_length=255)
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'goods_param_value'


class GoodsSku(models.Model):
    sku_id = models.IntegerField(primary_key=True)
    goods = models.ForeignKey('Goods', models.DO_NOTHING,related_name='goods_sku')
    name = models.CharField(max_length=20)
    values = models.CharField(max_length=100)
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'goods_sku'


class GoodsCategory(models.Model):
    cate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'goods_category'


class GoodsSubcategory(models.Model):
    sub_id = models.AutoField(primary_key=True)
    cate = models.ForeignKey('GoodsCategory', models.DO_NOTHING,related_name='cates')
    name = models.CharField(max_length=50)
    status = models.IntegerField()
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'goods_subcategory'


class GoodsType(models.Model):
    type_id = models.AutoField(primary_key=True)
    sub = models.ForeignKey('GoodsSubcategory', models.DO_NOTHING,related_name='subs')
    name = models.CharField(max_length=50)
    status = models.IntegerField()
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField()

    class Meta:
        db_table = 'goods_type'


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    goods = models.ForeignKey('Goods', models.DO_NOTHING, blank=True, null=True,related_name='order_goods')
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True,related_name='user_orders')
    goods_count = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'order'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    goods = models.ForeignKey('Goods', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()
    img = models.CharField(max_length=100, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'review'


class User(AbstractUser):
    email = models.CharField(max_length=50,unique=True)
    realname = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    pay_password = models.CharField(max_length=100, blank=True, null=True)
    question = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    phone = models.CharField(unique=True, max_length=11,null=True)
    is_vip = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'


class UserLoc(models.Model):
    loc_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    detail_loc = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_loc'


class UserMsg(models.Model):
    user_msg_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    msg_title = models.CharField(max_length=100)
    msg_img = models.CharField(max_length=100, blank=True, null=True)
    msg_content = models.TextField()
    status = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(db_column='is-delete', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'user_msg'
