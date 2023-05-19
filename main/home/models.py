from django.db import models
from django.urls import reverse


# global category list

class category(models.Model):

    cate_name = models.CharField(max_length=260, unique=True)
    slug = models.SlugField(max_length=240, unique=True)
    cate_img = models.ImageField(upload_to='category_list')

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categorys")

    def __str__(self):
        return self.cate_name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})




# individual product list

class featured_product(models.Model):

    pro_name = models.CharField(max_length=50)
    pro_desc = models.TextField()
    pro_cate = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    pro_img = models.ImageField(upload_to='featured_products',null=True)
    price = models.IntegerField(null=True)

    class Meta:
        verbose_name = ("featured_product")
        verbose_name_plural = ("featured_products")

    def __str__(self):
        return self.pro_name

    def get_absolute_url(self):
        return reverse("featured_product_detail", kwargs={"pk": self.pk})


class leatest_product(models.Model):

    pro_name = models.CharField(max_length=150)
    pro_desc = models.TextField()
    pro_cate = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    pro_img = models.ImageField(upload_to='leatest_products', null=True)
    price = models.IntegerField()

    class Meta:
        verbose_name = ("leatest_products")
        verbose_name_plural = ("leatest_products")

    def __str__(self):
        return self.pro_name
    
    def get_absolute_url(self):
        return reverse("leatest_product_detail", kwargs={"pk": self.pk})
    