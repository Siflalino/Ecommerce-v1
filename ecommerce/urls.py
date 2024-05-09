"""
URL configuration for ecommerce project.

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
from shop.views import register_client
from shop.views import index, detail, inscription_success
from django.contrib.auth import views as auth_views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('shop.urls')),
#     path('sinscrire/', include('shop.urls')),
# ]

# urlpatterns = [
#     path('', include('shop.urls')),  # Assurez-vous que c'est votre première URL
#     path('admin/', admin.site.urls),
#     path('register/', register_client, name='register_client'),
#     path('detail/', detail, name='detail' ),
#     #path('register/', register_client, name='register_client'),
    
#     # ... Autres URLs du projet ...
# ]

# urlpatterns = [
#     path('', register_client, name='register_client'),  # Vue d'inscription comme vue par défaut
#     path('admin/', admin.site.urls),
#     path('register/', register_client, name='register_client'),  # Laissez cette ligne si nécessaire
#     path('inscription_success/', inscription_success, name='inscription_success'),  # Ajoutez une vue de succès
#     path('<int:myid>/', detail, name="detail"),
#     path('index/', index, name='home'),  # Assurez-vous que c'est votre première URL
#     # ... Autres URLs de votre application ...
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('shop.urls')),  # Inclure les URLs de votre application shop
#     path('register/', register_client, name='register_client'),
#     path('', index, name='home'),
#     path('<int:myid>/', detail, name='detail'),
#     path('inscription_success/', inscription_success, name='inscription_success'),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', register_client, name='register_client'),  # Page d'inscription par défaut
#     path('inscription_success/', inscription_success, name='inscription_success'),
#     path('register/', register_client, name='register'),  # URL pour le formulaire d'inscription
#     path('index/', index, name='home'),  # URL pour la page d'accueil
#     path('<int:myid>/', detail, name='detail'),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    # path('', register_client, name='register_client'),  # Page d'inscription par défaut
    # path('inscription_success/', inscription_success, name='inscription_success'),
    # path('register/', register_client, name='register'),  # URL pour le formulaire d'inscription
    # path('index/', index, name='home'),  # URL pour la page d'accueil
    # path('<int:myid>/', detail, name='detail'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
]