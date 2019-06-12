from django.conf.urls import url

from api.account import views

urlpatterns = [
    url('register/', views.resgister_views, name='register'),
    url('login/', views.login_views, name='login'),
    url('checkemail/', views.check_eamil, name='check_eamil'),
    url('active/', views.active_account, name='active')
]
