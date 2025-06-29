from django.contrib import admin
from .models import Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    #prepopulate slug field
    prepopulated_fields = {'slug' :('category_name',)}
    #list_display in front page
    list_display = ('category_name','slug')


admin.site.register(Category,CategoryAdmin)
