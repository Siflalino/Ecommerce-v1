from django.urls import path
from shop.views import index, detail, checkout, login_view, edit_profile, acceuil, alternative_detail
from .views import register_client, inscription_success, confirmation, profile, change_password, commenter_produit
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView




# urlpatterns = [
#     # ... Vos autres URLs ...S
#     path('register/', register_client, name='register_client'),
#     path('inscription_success/', inscription_success, name='inscription_success'),  # Ajoutez une vue de succès
# ]


# urlpatterns = [
#     path('register/', register_client, name='register_client'),
#     path('', index, name='home'),
#     path('<int:myid>', detail, name="detail"),
#     path('inscription_success/', inscription_success, name='inscription_success'),
# ]

# urlpatterns = [
#     path('register/', register_client, name='register_client'),
#     path('', index, name='home'),
#     path('<int:myid>/', detail, name='detail'),
#     path('checkout', checkout, name="checkout"),
#     path('inscription_success/', inscription_success, name='inscription_success'),
#     path('login', login_view, name='login'),
# ]


urlpatterns = [
    path('register/', register_client, name='register_client'),
    path('index/', index, name='home'),
    path('<int:myid>/', detail, name='detail'),
    path('alternative_detail/<int:myid>/', alternative_detail, name='alternative_detail'),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation"),
    path('inscription_success/', inscription_success, name='inscription_success'),
    path('login/', login_view, name='login'),  # Utilisez votre vue de connexion personnalisée
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(template_name='shop/logout.html'), name='logout'),
    path('modifie_profile/', edit_profile, name='modifie_profile'),
    path('', acceuil, name='acceuil'),
    path('change_password/', change_password, name='change_password'),
    path('commentaire/<int:produit_id>/', commenter_produit, name='commenter_produit'),
]



