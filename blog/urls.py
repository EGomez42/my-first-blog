from django.conf.urls import url
from . import views

urlpatterns = [

	# Si la url tiene -->  r'^$'  Indica una expresion regular
	# Indica que sera la pagina inicial (home) de nuestro proyecto 
	url(r'^$', views.post_list, name='post_list'),
	# Observar post's a detalle
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	# Url para CRear un Nuevo Post
	url(r'^post/new/$', views.post_new, name='post_new'),
	# Url para Editar un Post
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]