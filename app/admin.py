from django.contrib import admin
from app.models import Category, EntryField


# class EntryFieldAdmin(admin.ModelAdmin):
#     list_display = 

admin.site.register(Category)
admin.site.register(EntryField)
