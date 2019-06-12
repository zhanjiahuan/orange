from django.contrib import admin
from django.conf.urls import url, include

from api.main import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.main),
    url('api/', include('api.main.urls')),
    url('detail/', include('api.detail.urls')),
    url('account/', include('api.account.urls')),
    url('person/', include('api.person.urls')),
]
