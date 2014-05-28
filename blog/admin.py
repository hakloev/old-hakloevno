from django.contrib import admin
from blog.models import Blogpost, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blogpost)
admin.site.register(Category)
