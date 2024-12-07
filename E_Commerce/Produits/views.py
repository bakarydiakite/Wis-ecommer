from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse     


def accueil(request):
    categories = Categories.objects.all()
    produit = MesProduits.objects.all()
    return render(request,'Produits/Accueil.html',{'produit':produit, 'categories':categories})


def details(request, my_id):
    produit = get_object_or_404(MesProduits,id=my_id)
    return render(request, 'Produits/detail.html', {'produit': produit})

def produits(request):
    categorie = Categories.objects.all()
    allProduit = MesProduits.objects.all()
    return render(request, 'Produits/Produits.html', {'allProduit': allProduit, 'categorie':categorie})
    
     
def recherches(request):
    if request.method == 'GET': 
        user_saisie = request.GET.get('recherche') 
        prods = MesProduits.objects.filter(nom__icontains=user_saisie)
        return render(request,'Produits/recherce.html',{'prods':prods})
    return render(request,'Produits/recherce.html')

#  Fonciton pour tout les categories

def prodCategorie(request,id_cate):
    categorie = Categories.objects.all()
    cat = Categories.objects.get(id=id_cate)
    print(cat)
    prodsCategorie = MesProduits.objects.filter(categorie=cat)
    return render(request,'Produits/catproduts.html',{'prodsCategorie':prodsCategorie,
                                                      'cate':cat,
                                                      'categorie':categorie})
    

# Fonction pour ajouter dans le panier
def addCart(request, idproduct):
    user = request.user
    product = get_object_or_404(MesProduits, id=idproduct)
    panier, _= Panier.objects.get_or_create(user=user)
    order, created = PanierOrder.objects.get_or_create(user=user, ordered=False, order=product)
    if created:
        panier.produits.add(order)
        panier.save()
    else :
        order.quantity +=1
        order.save()
    return redirect('produits')


#  Fonction pour le panier

def panier(request):
    user = request.user
    panier, create = Panier.objects.get_or_create(user=user)
    allproduct = panier.produits.all()
    # total = sum(item.prix() for item in allproduct)
    return render(request,'Produits/panier.html', {'allproduct':allproduct})

 
def supprimer_panier(request):
    if panier := request.user.panier:
        panier.delete()
    return redirect('accueil')

def commander(request):
    if request.method == "POST":
        items = request.POST.get('items')
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        notes = request.POST.get('notes')
        com = Commander(items=items, prenom=prenom,nom=nom, adresse=adresse, 
                        telephone=telephone, email=email, notes=notes)
        com.save()
    return render(request, 'Produits/commander.html')
