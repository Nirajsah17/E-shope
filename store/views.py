from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import category
from .models.customer import Customer
# Create your views here.
def index(request):
    product= None
    categories = category.get_all_caregory()
    CategoryId = request.GET.get('category')
    if CategoryId :
        product = Product.get_all_product_By_Category_Id(CategoryId )
    else:
        product = Product.get_all_product()
    data={}
    data['products'] = product
    data['categories'] = categories
    return render(request,'index.html',data)
def signup(request):
    if request.method =='GET':
        return render(request,'signup.html')
    else:
        PostData = request.POST
        first_name = PostData.get('fname')
        last_name = PostData.get('lname')
        phone = PostData.get('phone')
        email = PostData.get('email')
        password = PostData.get('password')
        customer = Customer(first_name=first_name,
                            Last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        customer.register()
        msg='successfully registered'
        return render(request,'signup.html',{'msg':msg})