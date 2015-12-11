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
]