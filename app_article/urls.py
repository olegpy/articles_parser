from django.conf.urls import include, url
from django.contrib import admin

from .views import parser

urlpatterns = [
    url(r'^', include('articles.urls'), name='articles'),
    url(r'^parser/$', parser, name='parser'),
    url(r'^admin/', include(admin.site.urls)),
]
