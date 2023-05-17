from django.db import models
from django.urls import reverse


# global category list

class category(models.Model):

    cate_name = models.CharField(max_length=260, unique=True)
    slug = models.SlugField(max_length=240, unique=True)
    cate_img = models.ImageField(upload_to='media')

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categorys")

    def __str__(self):
        return self.cate_name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})




# individual product list

class product(models.Model):

    pro_name = models.CharField(max_length=50)
    pro_desc = models.CharField(max_length=200)
    pro_cate = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    pro_img = models.ImageField(upload_to='products',null=True)
    price = models.IntegerField(null=True)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.pro_name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    