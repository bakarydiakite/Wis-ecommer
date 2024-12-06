from django.contrib import admin

from .models import MesProduits, Categories, PanierOrder, Panier, Commander


class AdminCategories(admin.ModelAdmin):
    list_display = ('nom_categorie', 'date_ajout')


class AdminProduits(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'categorie', 'date_ajout')

admin.site.register(MesProduits, AdminProduits)
admin.site.register(Categories, AdminCategories)


admin.site.register(PanierOrder)
admin.site.register(Panier)
admin.site.register(Commander) 
 

