from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redirige a la página de login antes de cargar las rutas de la aplicación
    path('', lambda request: redirect('/accounts/login/', permanent=False)),  
    # Incluye las URLs de la aplicación 'glownaturals'
    path('Gamer/', include('Gamer.urls')),
    # Incluir las rutas de login/logout de Django
    path('accounts/', include('django.contrib.auth.urls')),
]