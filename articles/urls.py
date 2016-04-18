from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='article_list'),
    url(r'^(?P<pk>\d+)/$',
        views.PostDetailView.as_view(), name='article_detail'),

]
