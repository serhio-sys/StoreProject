from django.contrib import admin
from .models import Item,Category,SubCategory,Raiting,Comments

class ItemAdm(admin.ModelAdmin):
    list_display = ("id","name","basket")
    list_display_links = ("name","basket")
    search_fields = (("id"),("name"))

class CategoryAdm(admin.ModelAdmin):
    list_display = ("id","name")
    list_display_links = ("name",)
    search_fields = (("id"),("name"))

admin.site.register(Item,ItemAdm)
admin.site.register(Category,CategoryAdm)
admin.site.register(SubCategory)
admin.site.register(Comments)
admin.site.register(Raiting)