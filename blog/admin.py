from django.contrib import admin
from .models import Post # Включаем модель Post

admin.site.register(Post) # Делаем чтобы модель была доступна из админки
