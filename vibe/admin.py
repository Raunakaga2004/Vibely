from django.contrib import admin
from .models import Vibe


# class VibeMediaInline(admin.TabularInline):
#     model = VibeMedia
#     extra = 1
#     max_num = 5


@admin.register(Vibe)   # ✅ attach custom admin
class VibeAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_at', 'media']


# @admin.register(VibeMedia)  # ✅ still register VibeMedia separately
# class VibeMediaAdmin(admin.ModelAdmin):
#     list_display = ['vibe', 'file']