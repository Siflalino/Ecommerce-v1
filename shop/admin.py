from django.contrib import admin
from .models import categorie, product,client, Commande

# Register your models here.
admin.site.site_header = "Siflalino-shop"
admin.site.site_title = "Siflalino-shop"
admin.site.index_title = "administrateur-Siflalino-shop"




# class AdminCategorie(admin.ModelAdmin):
#     list_display = ('name', 'date_added')

# class AdminProduct(admin.ModelAdmin):
#     list_display = ('title', 'price', 'category', "date_added")

# # class AdminClient(admin.ModelAdmin):
# #     list_display = ('email', 'adress', 'ville', 'date_added')

# admin.site.register(product,AdminProduct )
# admin.site.register(categorie, AdminCategorie)
# admin.site.register(client)
# #admin.site.register(Client)


# # admin.site.register(client, AdminClient)


class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', "date_added")
    search_fields = ('title',)
    list_editable = ('price',)

class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'pays', 'ville', 'adresse', 'total','date_commande')

admin.site.register(categorie, AdminCategorie)
admin.site.register(product, AdminProduct)
admin.site.register(client)
admin.site.register(Commande, AdminCommande)