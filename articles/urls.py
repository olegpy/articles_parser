from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='article_list'),
    url(r'^ajax_view/$', views.ajax_view, name='ajax_view'),
    url(r'^(?P<pk>\d+)/$',
        views.PostDetailView.as_view(), name='article_detail'),
]
