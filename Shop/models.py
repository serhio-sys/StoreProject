from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from Users.models import Basket

User = get_user_model()

class Category(models.Model):
    name = models.CharField("Name",max_length=50)
    count = models.PositiveSmallIntegerField("COUNT")
    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('catlist',kwargs={'pk':self.pk})

    class Meta():
            verbose_name = "CATEGORY"
            verbose_name_plural = "CATEGORYs"
    
    
class SubCategory(models.Model):
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,null=True,blank=True,default=None)
    name = models.CharField("Name",max_length=50)

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategorys"

    def __str__(self):
        return self.name


class Item(models.Model):
    img = models.ImageField('IMG',upload_to='items')
    name = models.CharField("Name",max_length=50)
    desk = models.TextField("Desk")
    cost = models.PositiveIntegerField("Price")
    cat = models.ForeignKey(
        "Category", verbose_name="Category", on_delete=models.CASCADE
    )
    basket = models.ForeignKey(
        Basket,verbose_name="BASKET",on_delete=models.SET_NULL,default=None,blank=True,null=True
    )

    count = models.PositiveSmallIntegerField("COUNT")

    def __str__(self):
        return self.name
    
    def get_url_add(self):
        return reverse('add',kwargs={'pk':self.pk})

    def get_url_rem(self):
        return reverse('remove',kwargs={'pk':self.pk})
    
    def get_url_detail(self):
        return reverse('item', kwargs={'pk':self.pk})

    class Meta():
            verbose_name = "ITEM"
            verbose_name_plural = "ITEMs"
