from django.db import models


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


