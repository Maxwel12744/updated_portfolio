from django.contrib import admin
from .models import Project, Skill, ContactMessage

admin.site.register(Project)
admin.site.register(Skill)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created")
    readonly_fields = ("created",)
    search_fields = ("name", "email", "message")


