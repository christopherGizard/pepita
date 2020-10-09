from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Post
from .forms import PostForm

#Affiche la liste des billets du post
class ListePosts(ListView):
	model = Post

	context_object_name = "posts"

	template_name = "blog/liste.html"

	paginate_by = 10


#Affichage detaillé d'un post
class DetailPost(DetailView):
	model = Post

	context_object_name = 'post'

	template_name = "blog/detail_post.html"

#Creation d'un post
class CreationPost(CreateView):
	model = Post

	template_name = 'blog/creer_post.html'

	form_class = PostForm

	success_url = reverse_lazy('liste_post')

	def form_valid(self, form):
		form.instance.slug = form.cleaned_data['slug']
		return super(CreationPost, self).form_valid(form)

#Modification d'un post
class ModificationPost(UpdateView):
	model = Post

	template_name = 'blog/creer_post.html'

	#form_class = 

	#success_url = reverse_lazy()


