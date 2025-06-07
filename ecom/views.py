from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from product.models import ProductTable,CartTable
from django.db.models import Q
from django.contrib import messages
    
# Create your views here.
# def home(request):
#    return render(request,'base.html')




def user_login(request):
   data ={}
   if request.user.is_authenticated:
      if request.user.is_superuser:
         return redirect("/admin")
      else:
         return redirect("/")
      
      
      
   if request.method=="POST":
      uname=request.POST['username']
      upass=request.POST['password']
      
      if (uname=="" or upass==""):
         data['error_msg']="Fields cant be empty"
      elif(not User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + " user does not exist"
      else:
         user=authenticate(username=uname,password=upass)
         if user is None:
            data['error_msg']="Wrong password"
         else:
            login(request,user)
            if user.is_superuser:
               return redirect("/admin")
            else:
               return redirect("/")
   return render(request,'user/login.html',context=data)

def user_register(request):
   data ={}
   if request.user.is_authenticated:
      if request.user.is_superuser:
         return redirect("/admin")
      else:
         return redirect("/")
   if request.method=="POST":
      username=request.POST['username']
      password=request.POST['password']
      password2=request.POST['password2']
      
      if (username=="" or password=="" or password2==""):
         data['error_msg']="Fields cant be empty"
      elif(password!=password2):
         data['error_msg']="Password Does not matched"
      elif(User.objects.filter(username=username).exists()):
         data['error_msg']=username + " already exist"
      else:
         user=User.objects.create(username=username)
         user.set_password(password)
         user.save()
         return redirect("/")
   return render(request,'user/register.html',context=data)



def user_logout(request):
   logout(request)
   return redirect('/')




def admin_panel(request):
   if request.user.is_authenticated:
      if not request.user.is_superuser:
         return redirect("/")

   return render(request,'admin/admin.html')
   
# ----------------------- all logics ---------------------------------
products=ProductTable.objects.none()
def home(request):
   data={}
   global products
   global filtered_products
   products=ProductTable.objects.filter(is_available=True)
   filtered_products=products
   data['products']=products
   user_id=request.user.id
   cart=CartTable.objects.filter(uid=user_id)
   data['cartvalue']=cart.count()
   return render(request,'base.html',context=data)


def filter_by_category(request,category_value):
   data={}
   #select * from product where is_available=True and category=category_value
   #from django.db.models import Q
   q1 = Q(is_available=True)
   q2 = Q(category=category_value)
   global products
   global filtered_products
   filtered_products=products.filter(q1 & q2)
   data['products']=filtered_products
   return render(request,'base.html',context=data)

def sort_by_price(request,sort_value):
   data={}
   global filtered_products
   #select * from product where is_available=True order by price desc
   if(sort_value=='asc'):
      sorted_products=filtered_products.filter(is_available=True).order_by('price')
   else:
      sorted_products=filtered_products.filter(is_available=True).order_by('-price')
   data['products']=sorted_products
   return render(request,'base.html',context=data)
 
def search_by_price_range(request):
   print("in search")
   data={}
   min=request.POST["min"]
   max=request.POST["max"]
   q1=Q(is_available=True)
   q2=Q(price__gte=min)
   q3=Q(price__lte=max)
   searched_products= filtered_products.filter(q1 & q2 & q3)
   data['products'] =searched_products
   return render(request,'base.html',context=data)
def add_to_cart(request,product_id ):
   if request.user.is_authenticated:
      user=request.user
      product=ProductTable.objects.get(id=product_id)
      q1=Q(uid=request.user.id)
      q2=Q(pid=product_id)
      cart_values=CartTable.objects.filter(q1 & q2)
      if (cart_values.count()>0):
         messages.error(request, "Product is already in your cart")
      else:
         cart=CartTable.objects.create(uid=user,pid=product,quantity=1)
         cart.save()
         messages.success(request, "Product is addedd in your cart")
      return redirect("/")
   else:
      return redirect("/login")
   

def find_cart_value(request):
   user_id=request.user.id
   cart=CartTable.objects.filter(uid=user_id)
   cart_count=cart.count()
   return cart.count()

def show_cart(request):
   data={}
   total_items=0
   total_price=0
   cart_count=find_cart_value(request)
   data['cartvalue']=cart_count
   products_in_cart=CartTable.objects.filter(uid=request.user.id)
   data['cartproducts']=products_in_cart
   for product in products_in_cart:
      total_items+=product.quantity
      total_price+=(product.pid.price*product.quantity)
   data['total_items']=total_items
   data['total_price']=total_price
   return render(request,'home/show_cart.html',context=data) 



def delete_cart(request,cart_id):
   cart=CartTable.objects.get(id=cart_id)
   cart.delete()
   return redirect("/cart")


def update_cart_quantity(request, flag, cart_id):
    # Retrieve the cart item with the given ID
    cart = CartTable.objects.filter(id=cart_id)
    
    if not cart.exists():
        # Handle the case where the cart item does not exist
        return redirect("/cart")

    # Get the cart item instance
    cart_item = cart[0]
    actual_quantity = cart_item.quantity

    if flag == 'inc':
        # Increase the quantity by 1
        cart_item.quantity = actual_quantity + 1
        cart_item.save()
    else:
        # Decrease the quantity by 1 if it's greater than 1
        if actual_quantity > 1:
            cart_item.quantity = actual_quantity - 1
            cart_item.save()
        else:
            # Remove the item from the cart if quantity is 1 or less
            cart_item.delete()
    
    # Redirect to the cart page
    return redirect("/cart")


def show_order(request):
   data={}
   total_items=0
   total_price=0
   cart_count=find_cart_value(request)
   data['cartvalue']=cart_count
   products_in_cart=CartTable.objects.filter(uid=request.user.id)
   data['cartproducts']=products_in_cart
   for product in products_in_cart:
      total_items+=product.quantity
      total_price+=product.pid.price
   data['total_items']=total_items
   data['total_price']=total_price
   return render(request, 'home/show_order.html',context=data)
      



import razorpay
def make_payment(request):
    # Initialize Razorpay client
    client = razorpay.Client(auth=("rzp_test_miMD0bZvjvilhm", "rZZmeUE3xkEOFprinJt7G3By"))

    # Create an order
    data = {
        "amount": 50000,  # Amount should be in paise (e.g., 500.00 INR = 50000 paise)
        "currency": "INR",
        "receipt": "order_rcptid_11"
    }

    try:
        # Create Razorpay order
        payment = client.order.create(data=data)
        payment_id = payment['id']  # Get the order ID from Razorpay response
        amount = data['amount']  # Get the amount from the data dictionary
    except Exception as e:
        print(f"Error creating Razorpay order: {e}")
        # Handle the error as needed, possibly return an error page or message
        return render(request, 'error_page.html', {'error': str(e)})

    # Pass payment_id and amount to the template
    return render(request, 'order_detail.html', {'payment_id': payment_id, 'amount': amount})
from django.shortcuts import render

def order_detail(request, payment_id, amount):
    # Process the order details using payment_id and amount
    # You can add your order logic here or retrieve the order from your database

    # Pass the payment ID and amount to the template
    return render(request, 'home/order_details.html', {'payment_id': payment_id, 'amount': amount})

# ------------


def product_details(request, id):
    product = get_object_or_404(ProductTable, id=id)
    return render(request, 'home/prod_detail.html', {'product': product})