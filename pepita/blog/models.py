from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Models
class Post(models.Model):
	#Titre du billet
	titre = models.CharField(max_length=200)
	#Le slug
	slug = models.SlugField(max_length=200)
	#Contenu du billet
	contenu = models.TextField()
	#une photo 
	photo = models.ImageField(upload_to="img/posts/")
	#La date de creation
	creation_date = models.DateField(default=timezone.now)
	#La date de modification
	modification_date = models.DateField(default=timezone.now)
	#Les tags decrivant le post
	tags = TaggableManager()

	class Meta:
		ordering = ['-modification_date']

	def __str__(self):
		return self.titre

class Commentaire(models.Model):
	#L'auteur du commentaire
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#Le contenu du commentaire
	contenu = models.TextField()
	#La date de creation du commentaire
	creation_date = models.DateField(default=timezone.now)
	#La date de modification du commentaire
	modification_date = models.DateField(default=timezone.now)
	#Le post concerné par le commentaire 
	post = models.ForeignKey('Post', on_delete=models.CASCADE)

	class Meta:
		ordering = ['creation_date']

	def __str__(self):
		return self.user.username + " : " + self.contenu


	
