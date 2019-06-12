from django.conf.urls import url

from api.main import views

urlpatterns = [
    url('cate/', views.CateView.as_view()),
    url('subs/', views.GoodsSubView.as_view()),
    url('goods/', views.GoodsView.as_view()),
]
