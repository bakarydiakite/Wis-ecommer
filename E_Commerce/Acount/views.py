from django.shortcuts import render,redirect
from .models import Utilisateur
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm  # Import du formulaire personnalisé

def inscription(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pw = request.POST.get("pw")
        pwConfirm  = request.POST.get("pwConfirm")
        
        user = Utilisateur.objects.create_user(
            username = username, 
            email = email,
            password = pw,
            confirm_pwd = pwConfirm
        )
        user.save()
    return render(request,"Acount/connexion.html")


def connexion(request):
    erreur = ""
    if request.method == "POST":
        username = request.POST.get("usernam")
        pw = request.POST.get("pwd")
        
        user = authenticate(username = username,
                            password = pw)
        if user is not None:
            login(request,user)
            return redirect('accueil')
        else:
            erreur = "Information Incorrecte"
            return render(request,"Acount/connexion.html",{"erreur":erreur})
    return render(request,"Acount/connexion.html")

def deconnexion(request):
    logout(request)
    return redirect("accueil")


def recuperation(request):
    return render(request, 'Acount/pwoublie.html')




class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'Acount/password_reset.html'
    email_template_name = 'Acount/password_reset_done.html'
    form_class = CustomPasswordResetForm  # Lien avec le formulaire personnalisé
    success_url = reverse_lazy('password_reset_done')

    
        
        