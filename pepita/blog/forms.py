from django import forms
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('titre', 'contenu', 'photo','tags')


	def clean(self):
		cleaned_data = super().clean()
		titre = cleaned_data.get("titre")
		slug = cleaned_data.get("slug")

		if not slug and titre:
			print("On slugify sa race")
			cleaned_data["slug"] = slugify(titre)

		return cleaned_data
	