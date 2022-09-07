from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    email = models.EmailField("EMAIL", max_length=254, unique=True,default=None)
    balance = models.PositiveIntegerField("MONEY",default=0)
    image = models.ImageField("IMAGE", upload_to="users/",default='users/def.png')
    kor = models.ForeignKey("Basket",verbose_name="KORZINA",on_delete=models.CASCADE, null=True, blank=True, default=None)
    activeEmail = models.BooleanField("ACTIVE EMAIL",default=False)

    def get_url_update_photo(self):
        return reverse("change",kwargs={"pk":self.pk})

    def __str__(self):
        return self.username

    class Meta():
            verbose_name = "User"
            verbose_name_plural = "Users"

class Basket(models.Model):
    user = models.ForeignKey(
       CustomUser, verbose_name="USER", on_delete=models.CASCADE
        )
    count = models.PositiveSmallIntegerField("COUNT",default=0)

    def __str__(self):
        return self.user.username

    def AllPrice(self):
        allprice = 0
        if self.count >= 1:
            for i in self.item_set.all():
                if i.count>1:
                    for num in range(0,i.count):
                        allprice += i.cost
                else:
                    allprice += i.cost
        return allprice
             
    
    class Meta():
            verbose_name = "BASKET"
            verbose_name_plural = "BASKETs"