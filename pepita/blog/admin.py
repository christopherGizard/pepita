from django.contrib import admin

from blog.models import Post, Commentaire

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'slug', 'titre', 'contenu', 'photo', 'creation_date', 'modification_date')

	list_filter = ('tags',)

	date_hierarchy = 'creation_date'

	ordering = ('creation_date',)

	search_fields = ('titre','contenu', 'tags',)

class CommentaireAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'contenu', 'post', 'creation_date', 'modification_date')

	list_filter = ('user', 'post',)

	date_hierarchy = 'creation_date'

	ordering = ('creation_date',)

	search_fields = ('contenu',)



admin.site.register(Post, PostAdmin)
admin.site.register(Commentaire, CommentaireAdmin)

