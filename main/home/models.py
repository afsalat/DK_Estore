from django.db import models
from django.urls import reverse


# global category list

class category(models.Model):

    cate_name = models.CharField(max_length=260, unique=True)
    slug = models.SlugField(max_length=240, unique=True)
    cate_img = models.ImageField(upload_to='category_list')

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.cate_name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})




# featured product list

class featured_product(models.Model):

    types = (('ft','featured'),)

    pro_name = models.CharField(max_length=50)
    pro_desc = models.TextField()
    pro_cate = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    pro_img = models.ImageField(upload_to='featured_products',null=True)
    pro_sizes = models.IntegerField(null=True)
    pro_colors = models.CharField(max_length=150,null=True)
    pro_price = models.IntegerField(null=True)
    pro_stock = models.IntegerField(null=True)
    pro_type = models.CharField(max_length=50, choices=types, default=types, null=True)

    class Meta:
        verbose_name = ("featured_product")
        verbose_name_plural = ("featured_products   ( max 12 items )")

    def __str__(self):
        return self.pro_name

    def get_absolute_url(self):
        return reverse("featured_product_detail", kwargs={"pk": self.pk})


# leatest product list

class leatest_product(models.Model):

    types = (('lt','leatest'),)

    pro_name = models.CharField(max_length=150)
    pro_desc = models.TextField()
    pro_cate = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    pro_img = models.ImageField(upload_to='leatest_products', null=True)
    pro_sizes = models.IntegerField(null=True)
    pro_colors = models.CharField(max_length=150,null=True)
    pro_price = models.IntegerField(null=True)
    pro_stock = models.IntegerField(null=True)
    pro_type = models.CharField(max_length=50, choices=types, default=types ,null=True)

    class Meta:
        verbose_name = ("leatest_products")
        verbose_name_plural = ("leatest_products  ( max 12 items )")

    def __str__(self):
        return self.pro_name
    
    def get_absolute_url(self):
        return reverse("leatest_product_detail", kwargs={"pk": self.pk})
    

class footer_details(models.Model):

    company_name = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=350)
    email_id = models.EmailField(max_length=254)
    contact_number = models.IntegerField()
    warning_message = models.CharField(max_length=50)
    twitter_link = models.CharField(max_length=250)
    facebook_link = models.CharField(max_length=250)
    linkedln_link = models.CharField(max_length=250)
    instagram_link = models.CharField(max_length=250)

    c_d = "Company Details"

    def __str__(self):
        return self.c_d
    



class register(models.Model):

    username = models.CharField(max_length=150)
    email_id = models.EmailField(max_length=254)
    password = models.CharField(max_length=550)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = ("Customer login status")
        verbose_name_plural = ("Customer login status")


