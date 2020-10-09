from django import forms
from django.contrib.auth.models import User
import re

#Formulaire de connexion d'un utilisateur
class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


#Formulaire pour enregistrer un nouveau profil
class NouveauUserForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur *", max_length=30, help_text="Caractères autorisés : Lettre, Chiffre, _, @, ., + et -")
	first_name = forms.CharField(label="Prénom", max_length=100, required=False)
	last_name = forms.CharField(label="Nom de famille", max_length=100, required=False)
	email = forms.EmailField(label="Adresse mail valide *")
	password = forms.CharField(label="Mot de passe *", widget=forms.PasswordInput)
	password_verification = forms.CharField(label="Verification mot de passe *", widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data["username"].lower()
		r = User.objects.filter(username=username)
		#Si le pseudo est deja pris
		if r.count():
			raise forms.ValidationError("Ce nom d'utilisateur existe déjà !")
		#Si le nom n'est pas correcte 
		if not re.fullmatch(r"[a-zA-Z0-9_.+-@]+", username):
			raise forms.ValidationError("Ce nom d'utilisateur contient des symboles non autorisés")

		return username

	def clean_email(self):
		email = self.cleaned_data["email"]
		r = User.objects.filter(email=email)
		#Si l'adresse est deja prise
		if r.count():
			raise forms.ValidationError("Cet email est deja utilisée. Choisissez en une autre")
		#Si ce n'est pas une adresse
		if not re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
			raise forms.ValidationError("Ceci n'est pas une adresse mail !")
		return email

	def clean_password_verification(self):
		password = self.cleaned_data["password"]
		password_verification = self.cleaned_data["password_verification"]

		if password and password_verification and password != password_verification:
			raise forms.ValidationError("Les mots de passes sont différents")

		return password_verification