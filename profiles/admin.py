from django.contrib import admin
from .models import Profile


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, UserAdmin)

