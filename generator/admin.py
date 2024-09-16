from django.contrib import admin

from generator.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """Админка видео"""
    list_display = ("pk", "title", "description", "uploaded_at")
