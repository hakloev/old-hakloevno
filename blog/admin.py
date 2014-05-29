from django.contrib import admin
from blog.models import Blogpost, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    exclude = ['slug']
    

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']

admin.site.register(Blogpost, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
