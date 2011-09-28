from django.contrib import admin
from very_poetic_nu.poems.models import Poem
from guardian.admin import GuardedModelAdmin

class PoemAdmin(GuardedModelAdmin):
    list_display = ('id', 'user', 'title')
    search_fields = ('id', 'title', 'content')

    user_can_access_owned_objects_only = True

admin.site.register(Poem, PoemAdmin)