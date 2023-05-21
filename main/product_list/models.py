from django.db import models
from home.models import category


class all_pro_list(models.Model):

    pro_name = models.CharField(max_length=150)
    pro_desc = models.TextField()
    pro_cate = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    pro_img = models.ImageField(upload_to='all_products',null=True)
    pro_sizes = models.IntegerField()
    pro_colors = models.CharField(max_length=150)
    pro_price = models.IntegerField()
    pro_stock = models.IntegerField()

    def __str__(self):
        return self.pro_name

