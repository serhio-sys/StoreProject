from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Basket
User = get_user_model()

class Basket_adm(admin.ModelAdmin):
    list_display = ("id","user","count")
    list_display_links = ("user",)
    search_fields = (("id"),)

class User_adm(admin.ModelAdmin):
    list_display = ('id',"username",'email')
    list_display_links = ("username",)
    search_fields = (("id"),("username"),)

admin.site.register(Basket,Basket_adm)
admin.site.register(User,User_adm)