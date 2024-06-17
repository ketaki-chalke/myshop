from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Feedback
from .forms import FeedbackForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
class IndexView(View):
  def get(self,request):
    user="ketaki"
    product_numb=4
    products = Product.objects.all().order_by('id')[:4]
    return render(request,"products/home.html",{
    "name":user,
    "number":product_numb,
    "products":products,
  })
  def post(self,request):
    pass



def sign_up(request):
  return render(request,"products/SignUp.html")

def login(request):
  return render(request,"products/login.html")


def logout_view(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

def mypage(request):
  return render(request,"products/mypage.html")


def product_cat(request,product):
  if product=="suits" or product=="dresses" or product=="shirts" or product=="shoes":
     return HttpResponse(f"Here is the list of our {product} !")
  else:
    return HttpResponse(f"The {product} is not available")
  
class ProductPageView(View):
  def get(self,request,product_brand,product_slug):
     product = Product.objects.get(slug = product_slug)
     form = FeedbackForm()
     reviews = Feedback.objects.filter(product=product)
     return render(request,"products/product.html",{
        "product":product,
        "form":form,
        "reviews":reviews
    })
  def post(self,request,product_brand,product_slug):
    product = Product.objects.get(slug = product_slug)
    form = FeedbackForm(request.POST)
    reviews = Feedback.objects.filter(product=product)
    if form.is_valid():
       feedback = Feedback(
         name = form.cleaned_data["name"],
         rating = form.cleaned_data["rating"],
         product = product,
         text = form.cleaned_data["text"]
       )
       feedback.save()
       messages.success(request,"Your feedback was submitted successfully !")
       

       return render(request,"products/product.html",{
         "product":product,
         "form":form,
         "reviews":reviews
    })

