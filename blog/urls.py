from django.conf.urls import url
from . import views

urlpatterns = [

	# Si la url tiene -->  r'^$'  Indica una expresion regular
	# Indica que sera la pagina inicial (home) de nuestro proyecto 
	url(r'^$', views.post_list, name='post_list'),
	# Observar post's a detalle
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

]