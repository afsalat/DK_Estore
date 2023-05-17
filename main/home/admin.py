from django.contrib import admin
from .models import product,category

# Register your models here.

class cateadmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('cate_name','cate_img')}

admin.site.register(category,cateadmin)


admin.site.register(product)