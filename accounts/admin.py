from django.contrib import admin
from .models import Profile

# Register your models here.

# PROFILE DETALLADO
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'city', 'phone', 'user_groups')
    search_fields = ('country', 'city', 'user__groups__name')
    list_filter = ('country', 'city', 'user__groups')

    def user_groups(self, obj):
        return ", ".join([group.name for group in obj.user.groups.all()])
    
    user_groups.short_description = 'Grupos'

admin.site.register(Profile, ProfileAdmin)