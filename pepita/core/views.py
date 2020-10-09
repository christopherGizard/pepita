from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ConnexionForm, NouveauUserForm

# Create your views here.
def accueil(request):
	return render(request,'core/accueil.html', locals())

"""
Les vues de connexion
"""
def connexion(request):
	error = False

	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
				return redirect('accueil')
			else: # sinon une erreur sera affichée
				error = True
	else:
		form = ConnexionForm()

	return render(request, 'core/connexion.html', locals())

def deconnexion(request):
	logout(request)
	return redirect('accueil')

"""
Creation profil
"""
def nouveauUser(request):

	if request.method == "POST":
		form = NouveauUserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			
			user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

			return redirect('accueil')
	else:
		form = NouveauUserForm()

	return render(request, 'core/nouveau_user.html', locals())