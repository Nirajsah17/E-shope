from django.contrib import admin
from .models.product import Product
from .models.category import category
from .models.customer import Customer



class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category','description','image']
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','Last_name','phone','email','passoword']
# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(category,AdminCategory)
admin.site.register(Customer)
