from django.contrib import admin
from apps.blog.models import Blogpost, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ('slug',)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']

admin.site.register(Blogpost, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
