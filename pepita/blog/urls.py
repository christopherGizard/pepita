from django.urls import path
from . import views

urlpatterns = [
	path('', views.ListePosts.as_view(), name="liste_post"),
	path('creer-post', views.CreationPost.as_view(), name="creer_post"),


]