from django.contrib import admin
from .models import Book
class studentview(admin.ModelAdmin):
    list_display=[
        'name',
        'author',
        'price',
        'publish_date',
    ]
admin.site.register(Book,studentview)

