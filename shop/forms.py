from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import client, Profile, Commentaire
from django.contrib.auth import get_user_model

class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['nom', 'prenom', 'email', 'pays', 'ville', 'adresse', 'mot_de_passe', 'validé_mot_de_passe']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'nom', 'prenom', 'email', 'pays', 'ville', 'adresse']


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['note', 'commentaire']
