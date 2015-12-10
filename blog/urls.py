from django.conf.urls import url
from . import views

urlpatterns = [

	# Si la url tiene -->  r'^$'  Indica una expresion regular
	# Indica que sera la pagina inicial (home) de nuestro proyecto 
	url(r'^$', views.post_list, name='post_list'),

]