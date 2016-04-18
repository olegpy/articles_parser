from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('articles.urls'), name='articles'),
    url(r'^admin/', include(admin.site.urls)),
]
