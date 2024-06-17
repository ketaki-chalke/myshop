from django.urls import path
from . import views

urlpatterns = [
     path('',views.IndexView.as_view(),name="home"),
     path('mypage',views.mypage,name="mypage"),
     path('products/<product>',views.product_cat,name="productcat"),# suit product category
     path('signup',views.sign_up,name="signup"),#signup of the user 
     path('products/<product_brand>/<product_slug>',views.ProductPageView.as_view(),name="product_page"),
     path('login',views.login,name="login"),
     path('logout/', views.logout_view, name='logout'),
]
