from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from taggit.models import Tag


from .models import Post
from .forms import PostForm

"""
Vues pour les posts
"""

#Affiche la liste des billets du blog
class ListePosts(ListView):
	model = Post

	context_object_name = "posts"

	template_name = "blog/liste.html"

	paginate_by = 5

	def get_context_data(self, *args, **kwargs):
		# Call the base implementation first to get a contexte
		context = super().get_context_data(*args)
		# On recupere les 20 tags les plus communs
		tags = Post.tags.most_common(1)[:20]
		context["tags"] = tags
		return context

#Affiche la liste des billets du blog
class ListePostsByTag(ListView):
	model = Post

	context_object_name = "posts"

	template_name = "blog/liste.html"

	paginate_by = 5

	def get_queryset(self):
		if 'tag' in self.kwargs:
			tags = [self.kwargs['tag']]
			return Post.objects.filter(tags__name__in=tags)

	def get_context_data(self, *args, **kwargs):
		# Call the base implementation first to get a contexte
		context = super().get_context_data(*args)
		# On recupere les 20 tags les plus communs
		tags = Post.tags.most_common(1)[:20]
		context["tags"] = tags
		if 'tag' in self.kwargs:
			context["current_tag"] = self.kwargs['tag']
		return context


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

	form_class = PostForm

	success_url = reverse_lazy('liste_post')

	def get_object(self):
		code = self.kwargs.get('id',None)
		slug = self.kwargs.get('slug', None)
		return get_object_or_404(Post,pk=code)

	def form_valid(self, form):
		form.instance.slug = form.cleaned_data['slug']
		return super(CreationPost, self).form_valid(form)

#Suppression d'un post
class SuppressionPost(DeleteView):
	model = Post

	template_name = "blog/suppression_post.html"

	success_url = reverse_lazy('liste_post')

	def get_object(self):
		code = self.kwargs.get('id',None)
		slug = self.kwargs.get('slug', None)
		return get_object_or_404(Post,pk=code)
"""
Vues pour les tags
"""

#Affiche la liste des tags
class ListeTags(ListView):
	model = Tag

	context_object_name = "tags"

	template_name = "blog/liste_tag.html"

	paginate_by = 50

	ordering = ['name']






