from django.conf.urls import url

from api.person import views

urlpatterns = [
    url('center',views.api_user_center),
]
