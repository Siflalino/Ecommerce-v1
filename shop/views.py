from django.shortcuts import render, redirect
from .models import product, Commande, client
from django.core.paginator import Paginator
from .forms import ClientForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import categorie
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CommentaireForm
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Si aucun profil n'existe pour cet utilisateur, créez-en un
        profile = Profile(user=request.user)
        profile.save()
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'shop/profile.html', {'form': form})


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Mettre à jour les informations de l'utilisateur actuellement connecté
            user = request.user
            user.first_name = form.cleaned_data['prenom']
            user.last_name = form.cleaned_data['nom']
            user.email = form.cleaned_data['email']
            user.pays = form.cleaned_data['pays']
            user.ville = form.cleaned_data['ville']
            user.adresse = form.cleaned_data['adresse']
            user.save()
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
                profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'shop/modifie_profile.html', {'form': form})


@login_required
def index(request):
    product_object = product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        product_object = product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 8)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object':product_object})



def detail(request, myid):
    product_object = product.objects.get(id=myid)
    products_same_category = product.objects.filter(category=product_object.category).exclude(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object, 'products_same_category': products_same_category})


def alternative_detail(request, myid):
    product_object = product.objects.get(id=myid)
    products_same_category = product.objects.filter(category=product_object.category).exclude(id=myid)
    return render(request, 'shop/alternative_detail.html', {'product': product_object, 'products_same_category': products_same_category})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Votre mot de passe a été mis à jour avec succès !')
            return redirect('profile')  # Rediriger vers la page de profil
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'shop/change_password.html', {'form': form})



from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import ClientForm, ProfileForm

def register_client(request):
    if request.method == 'POST':
        user_form = ClientForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Créer un utilisateur avec les données du formulaire
            user_data = user_form.cleaned_data
            myuser = get_user_model().objects.create_user(username=user_data['email'], password=user_data['mot_de_passe'])
            myuser.first_name = user_data['prenom']
            myuser.last_name = user_data['nom']
            myuser.email = user_data['email']
            myuser.save()

            # Créer un profil utilisateur avec les données du formulaire
            profile = profile_form.save(commit=False)
            profile.user = myuser
            profile.save()

            messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
            return redirect('login')  # Assurez-vous que 'login' est le nom correct de votre vue de connexion
    else:
        user_form = ClientForm()
        profile_form = ProfileForm()
    return render(request, 'shop/register.html', {'user_form': user_form, 'profile_form': profile_form})





def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['mot_de_passe']

        # Authentification de l'utilisateur
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie !')
            return redirect('home')
        else:
            messages.error(request, 'Adresse e-mail ou mot de passe incorrect.')
            return redirect('login')

    return render(request, 'shop/login.html')



def inscription_success(request):
    return render(request, 'shop/inscription_success.html')

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        adresse = request.POST.get('adresse')
        com = Commande.objects.create( items=items, nom=nom, email=email, pays=pays, ville=ville, adresse=adresse, total=total)
        com.save()
        return redirect('confirmation')
        
    return render(request,'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom

    return render(request, 'shop/confirmation.html', {'name': nom}) 


def votre_vue(request):
    categories = categorie.objects.all()
    return render(request, 'shop/index.html', {'categorie_objects': categories})

def logout_view(request):
    return redirect(reverse_lazy('logout'))

def acceuil(request):
    product_objects = product.objects.all()
    item_name = request.GET.get('item-name')
    
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)
    
    return render(request, 'shop/acceuil.html', {'product_objects': product_objects})


@login_required
def commenter_produit(request, produit_id):
    produit = get_object_or_404(product, id=produit_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.produit = produit
            commentaire.utilisateur = request.user
            commentaire.save()
            return redirect('detail', myid=produit_id)
    else:
        form = CommentaireForm()
    return render(request, 'shop/commentaire.html', {'form': form, 'produit': produit})