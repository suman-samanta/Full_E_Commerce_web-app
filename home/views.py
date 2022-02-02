from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from datetime import datetime
from home.models import Address, Cart, Contact, Orders, Products
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
# from django import forms 
from home.models import Products,Cart
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request) :
    productall=Products.objects.all()
    list=[productall]
    for i  in range(0,len(list)):
       list.append(i)
       product_name=Products.objects.all()[i]
    product=Products.objects.filter(product_name=product_name)
    context={'product':product,
             "i":i,
            'productall':productall,
        } 
    return render(request,'index.html',context=context)

@login_required             
def about(request):
    return render(request,'about.html')

@login_required 
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent! We will contact you soon!')
    return render(request,'contact.html')

def loginuser(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already Logged in")
        return redirect('/')
    if request.method=='POST':
      username=request.POST.get('name')
      email=request.POST.get('email')
      password=request.POST.get('password')
      user = authenticate(username=username,email=email,password=password)
      if user is not None:
          login(request,user)
          messages.success(request,"You are now Logged In")
          return redirect('/')
      else:
          messages.success(request,"Crediantials Incorrect! Please input the correct crediantials to log in")
          return render(request,'login.html')
      
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    messages.success(request,'You are Not logged in yet! Please Log in to see this content')
    return redirect('/login')

def signup(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already Logged in")
        return redirect('/')
    if request.method=="POST":
      username=request.POST.get('name')
      email=request.POST.get('email')
      password=request.POST.get('password')
      
      try:
         user = User.objects.create_user(username=username,email=email,password=password)
         messages.success(request, 'Your account has been created!')
         return redirect('/login')
      except  :
        #   user=User.objects.get(username=username)
          return redirect('/login')
          
    return render(request,'signup.html')


@staff_member_required
def add_a_product(request):
    if request.user.is_authenticated:
       if request.method=="POST": 
          product_name=request.POST.get('name')
          product_desc=request.POST.get('desc')
          product_price=request.POST.get('price')
          product_img=request.FILES.get('file')
          product_img2=request.FILES.get('file2')
          product_img3=request.FILES.get('file3')
          product=Products(product_name=product_name,product_img=product_img,product_desc=product_desc,product_price=product_price,product_img2=product_img2,product_img3=product_img3)
          product.save()
          messages.success(request, 'Products saved')
    else:
        messages.success(request,"Only staff member can add a product to our website")
        return redirect('/')

    return render(request,"product.html")

def product_view(request, pd_nm):
    product = Products.objects.filter(product_name=pd_nm).first()
    context={'product':product,
            } 
    return render(request,"product_view.html",context=context)

def add_to_cart(request,pd_nm):
   
    product = Products.objects.filter(product_name=pd_nm).first()
    # user=User.objects.get()
    current_user=request.user
    product_name=product.product_name
    product_price=product.product_price
    product_img=product.product_img
    print(current_user)
    cart_x = Cart.objects.filter(product_name=pd_nm,user=current_user).first()
    cart_all=Cart.objects.all()
    
    if cart_x in cart_all:
        cart_x.quantity = cart_x.quantity + 1
        cart_x.product_price=cart_x.quantity*product.product_price
        cart_x.save()
    else:
      cart=Cart(user=current_user,product_name=product_name,product_price=product_price,product_img=product_img)
      cart.save()
    messages.success(request,"Product Added To your cart")
    
    return redirect ("home")

def mycart(request):
    current_user=request.user
    try:
       cart_product_all=Cart.objects.filter(user=current_user)
       list=[cart_product_all]
       for i in range(0,len(list)):
          list.append(i)
          cart_product=Cart.objects.all()[i]
       cart_product_name=Cart.objects.filter(product_name=cart_product)
       context={"cart_product_all":cart_product_all,
             "cart_product_name":cart_product_name,
    }
    except:
        messages.success(request,"You have no product in the cart yet!")
        return redirect("/")

    return render(request,'mycart.html',context=context)

def remove_product_from_cart(request,pd_nm):
    cart_product_all=Cart.objects.all()
    cart_product=Cart.objects.filter(product_name=pd_nm)
    cart_product.delete()
    messages.success(request,"This Product has been removed from cart")
    return render(request,'mycart.html')

def buy_now(request,pd_nm):
    cart_product=Cart.objects.get(product_name=pd_nm)
    cart_product_all=Cart.objects.all()
    
    context={
        "cart_product":cart_product,
        "cart_product_all":cart_product_all
    }
    if request.method=="POST":
        username=request.POST.get('name')
        phone_number=request.POST.get('phone')
        address=request.POST.get('address')
        pin=request.POST.get('pin')
        address_x=Address(username=username,phone_number=phone_number,address=address,pin=pin)
        address_x.save()
        messages.success(request,'Your crediantials has been saved.Please OrderNow!')
    
    return render(request,"order_now.html",context=context)


def order_place(request,pd_nm):
    cart_product=Cart.objects.get(product_name=pd_nm)
    product_name=cart_product.product_name
    product_price=cart_product.product_price
    product_img=cart_product.product_img
    quantity=cart_product.quantity
    total_price=cart_product.total_price
    order=Orders(product_name=product_name,product_price=product_price,product_img=product_img,quantity=quantity,total_price=total_price)
    order.save()
    messages.success(request,"Pay now! to Place Your order")
    return render(request,"payment.html")
