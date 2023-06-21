from django.db import models
from home import models as mok




class cart(models.Model):

    pro_name = models.CharField(max_length=150)
    pro_desc = models.TextField()
    pro_cate = models.ForeignKey(mok.category, on_delete=models.CASCADE, null=True)
    pro_img = models.ImageField(upload_to='leatest_products', null=True)
    pro_sizes = models.IntegerField(null=True)
    pro_colors = models.CharField(max_length=150,null=True)
    pro_price = models.IntegerField(null=True)
    pro_stock = models.IntegerField(null=True)
    # person_id = 
    
# class order_details(models.Model):
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email_id = models.EmailField()
#     phone = models.IntegerField()
#     adddress_line1 = models.TextField()
#     adddress_line2 = models.TextField()
#     country = models.CharField(max_length=150)
    