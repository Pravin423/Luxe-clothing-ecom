from django.shortcuts import render,redirect
from product.models import ProductTable

# Create your views here.

def add_product(request):
   if request.method=='POST':
      name=request.POST.get('name')
      price=request.POST.get('price')
      description=request.POST.get('description')
      quantity=request.POST.get('quantity')
      category=request.POST.get('category')
      image = request.FILES.get('image')
      is_available=(request.POST.get('is_available',False)) and ('is_available' in request.POST)
      
      product=ProductTable.objects.create(name=name,price=price,description=description,quantity=quantity,category=category,image=image,is_available=is_available)
      
      product.save()
      
      return redirect("/admin/product/view/")
   return render(request,'admin/product/add_product.html')

def view_products(request):
   data={}
   products=ProductTable.objects.all()
   # print(products.count())
   data['products']=products
   return render(request,'admin/product/view_product.html',context=data)

def delete_product(request,productid):
   product=ProductTable.objects.get(id=productid)
   product.delete()
   return redirect("/admin/product/view/")





def update_product(request, productid):
    data = {}
    product = ProductTable.objects.get(id=productid)
    data['product'] = product  # Consistent context variable name
    if request.method == 'POST':
        product_name = request.POST.get('name')
        product_price = request.POST.get('price')
        product_description = request.POST.get('description')
        product_quantity = request.POST.get('quantity')
        product_category = request.POST.get('category')
        product_is_available = 'is_available' in request.POST

        # Update fields
        product.name = product_name
        product.price = product_price
        product.description = product_description
        product.quantity = product_quantity
        product.category = product_category
        product.is_available = product_is_available

        if 'image' in request.FILES:
            product.image = request.FILES['image']

        product.save()

        return redirect("/admin/product/view/")
    
    return render(request, 'admin/product/update_product.html', context=data)