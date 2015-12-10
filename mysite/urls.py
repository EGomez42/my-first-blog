from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    # Incluye/Busca/Trae todos los urls de la App blog
    url(r'', include('blog.urls')),

]
