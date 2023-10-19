from django.contrib import admin
from .models import Category, Post, Like, Comment

# Registrar modelos para que apareçam no admin
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
