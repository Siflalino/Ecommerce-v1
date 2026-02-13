from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
import random
import string

# Create your models here.
class categorie(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date_added"]

    @staticmethod
    def get_all_categories():
        return categorie.objects.all()

class product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(categorie, related_name="category", on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    disponibilite = models.BooleanField

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_added"]

    


class client(AbstractUser):
    nom = models.CharField(max_length=100, default='')
    prenom = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, unique=True)
    pays = models.CharField(max_length=300, default='')
    ville = models.CharField(max_length=300, default='')
    adresse = models.CharField(max_length=300, default='')
    mot_de_passe = models.CharField(max_length=128, default='')
    validé_mot_de_passe = models.CharField(max_length=128, default='')
    date_inscrit = models.DateTimeField(auto_now=True)


    REQUIRED_FIELDS = ['nom', 'prenom', 'pays', 'ville', 'adresse', 'mot_de_passe','validé_mot_de_passe']

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email  # Utiliser l'email comme username
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["-date_inscrit"]


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
    nom = models.CharField(max_length=100, default='')
    prenom = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, unique=True)
    pays = models.CharField(max_length=300, default='')
    ville = models.CharField(max_length=300, default='')
    adresse = models.CharField(max_length=300, default='')
    

class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=1000)
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pays = models.CharField(max_length=300)
    ville = models.CharField(max_length=300)
    adresse = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_commande"]

    def __str__(self):
        return self.nom
    

class Commentaire(models.Model):
    produit = models.ForeignKey('product', related_name='commentaires', on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    note = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    commentaire = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_commentaire']
