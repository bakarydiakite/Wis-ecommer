from django.contrib import admin
from django.urls import path
from Produits.views import accueil, details, produits, recherches, prodCategorie, panier, supprimer_panier, addCart, commander
from Acount.views import inscription, connexion, deconnexion
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views  # Import des vues intégrées pour la gestion des mots de passe
from Acount.forms import CustomPasswordResetForm  # Assure-toi que ce formulaire est défini dans forms.py
from Acount.views import CustomPasswordResetView  # La vue personnalisée pour la réinitialisation

urlpatterns = [
    # Routes principales 
    path('admin/', admin.site.urls),
    path('', accueil, name='accueil'),
    path('produit/<int:my_id>/', details, name='details'),
    path('produits/', produits, name='produits'),
    path('recherche/', recherches, name='recherche'),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('prodCategorie/<int:id_cate>/', prodCategorie, name='prodCategorie'),
    path('panier/', panier, name='panier'),
    path('panier/supprimer', supprimer_panier, name='supprimer_panier'),
    path('addcart/<int:idproduct>/', addCart, name='addCart'),
    path('commander/', commander, name='commander'),

    # Routes pour la récupération de mot de passe
    path(
        'password-reset/',
        CustomPasswordResetView.as_view(template_name='Acount/password_reset.html'),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='Acount/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='Acount/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='Acount/password_reset_complete.html'),
        name='password_reset_complete'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  