from django.contrib import admin
from .models import *

# Register your models here.
class productAdmin(admin.ModelAdmin):    
    list_display = ['id','name','category_name','descreption','buy_price','sell_price','quantity']


#admin register
admin.site.register(product,productAdmin)
