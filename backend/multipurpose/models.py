from django.db import models

# Create your models here.

category_choices = [('GRC','grocery'),
                    ('STA','stationery'),
                    ('HUS','house hold')]

class Products(models.Model):
    product_name = models.CharField(max_length=120)
    description = models.TextField()
    category = models.TextField(blank=False, choices = category_choices)

    def _str_(self):
        return self.title