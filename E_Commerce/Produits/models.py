from django.db import models
from Acount.models import Utilisateur
from E_Commerce.settings import AUTH_USER_MODEL
from django.utils import timezone


class Categories(models.Model):
    nom_categorie = models.CharField(max_length=30)
    date_ajout = models.DateTimeField(auto_now=True)
    image_categorie = models.ImageField(upload_to="img_categorie")
    description = models.TextField()
    def __str__(self): 
        return self.nom_categorie
    
    class Meta : 
        ordering = ['date_ajout']
    


class MesProduits(models.Model):
    image = models.ImageField(upload_to='img_produits')
    nom = models.CharField(max_length=30)
    prix = models.IntegerField()
    description = models.TextField()
    categorie = models.ForeignKey(Categories,on_delete=models.CASCADE)
    date_ajout = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.nom} à pour prix {self.prix}"
    

class PanierOrder(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    order = models.ForeignKey(MesProduits, on_delete=models.CASCADE)
    quantity =  models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    date = models.DateField(auto_now=True, blank=True, null=True)
    def __str__(self):
        return f"{self.order.nom} - {self.quantity}"
    
    def total_prix(self):
        return self.order.prix * self.quantity
    
    
       
class Panier(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    produits = models.ManyToManyField(PanierOrder)
    
    def __str__(self):
        return f"le panier de {self.user}"
    
    def delete(self, *args, **kwargs):
        for order in self.produits.all():
            order.ordered = True
            order.date = timezone.now()
            order.save()
        self.produits.clear()
        super().delete(*args, **kwargs)
        

class Commander(models.Model):
   prenom = models.CharField(max_length=50)
   nom = models.CharField(max_length=50)
   email = models.EmailField()
   adresse = models.CharField(max_length=200)
   telephone = models.IntegerField()
   notes = models.CharField(max_length=500)
   date = models.DateField(auto_now=True, blank=True, null=True)
   items = models.CharField(max_length=600)
   
   class Meta :
       ordering = ['-date'] 
    
