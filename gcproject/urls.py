from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('gcrestapp.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
]