from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main_page, name = 'main_page'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^search/', views.search, name='search'),
    url(r'^board_list/(?P<pk>[0-9]+)/$', views.board_list, name='board_list'),
    url(r'^board_view/(?P<pk>[0-9]+)/$', views.board_view, name='board_view'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^like-blog/', views.like_count_blog, name='like_count_blog'),
    url(r'^get_like/$', views.get_like, name='get_like'),
    url(r'^board_list/[0-9]+/post_list/(?P<pk>[0-9]+)$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/new/$', views.post_new, name='post_new'),
	url(r'^board/(?P<pk>[0-9]+)/new/$', views.board_new, name='board_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
]
