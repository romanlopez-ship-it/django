"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from . import views
'''
User = get_user_model()
try:
    # Intenta crear el superusuario usando el método oficial de Django
    User.objects.create_superuser('admin', 'admin@example.com', 'AdminUTEC2026*')
    print("¡Superusuario creado con éxito en producción!")
except IntegrityError:
    # Si el usuario ya existe, no hace nada y evita que el servidor falle
    pass
'''
urlpatterns = [
    path('admin/',       admin.site.urls),
    path('',             views.bienvenida,             name='inicio'),
    path('clientes/',    include('clientes.urls',    namespace='clientes')),
    path('proveedores/', include('proveedores.urls', namespace='proveedores')),
    path('productos/',   include('productos.urls',   namespace='productos')),
    path('ventas/',      include('ventas.urls',       namespace='ventas')),
    path('reportes/',    include('reportes.urls',     namespace='reportes')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

