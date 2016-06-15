from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.books_list, name="book_list"),
    url(r'^(?P<pk>[0-9]+)/$', views.books_detail, name="book_detail"),
    url(r'^author/(?P<pk>[0-9]+)/$', views.author_detail, name="author_detail"),
    
]
