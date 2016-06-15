from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^(?P<pk>[0-9]+)/$', views.news_detail, name='news_detail'),
    url(r'^(?P<pk>[0-9]+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^new/$', views.news_new, name='news_new'),
    
    
]
