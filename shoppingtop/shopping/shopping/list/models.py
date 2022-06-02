from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class List(models.Model):
    shop = models.CharField(max_length=100, default="")
    shop_items = models.TextField(default="")
    date = models.DateField(null=True, blank=True, default=datetime.today)
    shopper = models.ForeignKey(
            User,
            on_delete=models.CASCADE, default=""
        )
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.shop} {self.date}"

    def get_absolute_url(self):
        return f"/shoppinglist/{self.pk}" 

    def shop_items_better_list(self):
        return self.shop_items.split('\n')
