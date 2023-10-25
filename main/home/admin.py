from django.contrib import admin
from .models import featured_product,category,leatest_product,footer_details, register


# Register your models here.

class cateadmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('cate_name','cate_img')}

admin.site.register(category,cateadmin)


admin.site.register(featured_product)

admin.site.register(leatest_product)

admin.site.register(footer_details)

admin.site.register(register)