from django.urls import path
from . import views

urlpatterns = [
	path('', views.ListePosts.as_view(), name="liste_post"),
	path('byTag/<tag>', views.ListePostsByTag.as_view(), name="liste_post_by_tag"),
	path('creer-post', views.CreationPost.as_view(), name="creer_post"),
	path('modifier-post/<int:id>/<slug:slug>', views.ModificationPost.as_view(), name="modifier_post"),
	path('supprimer_post/<int:id>/<slug:slug>', views.SuppressionPost.as_view(), name="supprimer_post"),
	path('tags', views.ListeTags.as_view(), name="liste_tag"),


]