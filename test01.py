dic1 = [{
    "sub": {
        "cate": {
            "name": "衣服"
        },
        "name": "女装"
    },
    "name": "女士羽绒服"
}]

print(dic1[0].get('sub').get('name'))
print(dic1[0].get('sub').get('cate').get('name'))
print(dic1[0].get('name'))

# 女装
# 衣服
# 女士羽绒服
