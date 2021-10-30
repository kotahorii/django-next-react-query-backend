from django.contrib import admin
from .models import Blog, Tag, User

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Blog)
