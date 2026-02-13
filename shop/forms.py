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

#     def save(self, commit=True):
#         user = super(ClientRegistrationForm, self).save(commit=False)
#         # Set password randomly generated in the model
#         user.set_password(user.password1)
#         if commit:
#             user.save()
#         return user


# Client = get_user_model()      
# class ClientForm(forms.ModelForm):
#     password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
#     # password = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput)

#     class Meta:
#         model = client
#         fields = ['last_name', 'first_name', 'email', 'ville', 'adress', 'password']

    # def clean_password2(self):
    #     # Vérifie que les deux mots de passe correspondent
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Les mots de passe ne correspondent pas")
    #     return password2

    # def save(self, commit=True):
    #     # Sauvegarde le mot de passe haché
    #     client = super(ClientForm, self).save(commit=False)
    #     client.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         client.save()
    #     return client
