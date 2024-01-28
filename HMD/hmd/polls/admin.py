from django.contrib import admin

from .models import Users
from .models import Post
from .models import Categories

admin.site.register(Users)
admin.site.register(Post)
admin.site.register(Categories)