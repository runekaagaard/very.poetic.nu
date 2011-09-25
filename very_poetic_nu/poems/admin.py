from django.contrib import admin
from very_poetic_nu.poems.models import Poem

class PoemAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title')
    list_filter = ('author',)
    search_fields = ('id', 'title', 'content')

admin.site.register(Poem, PoemAdmin)