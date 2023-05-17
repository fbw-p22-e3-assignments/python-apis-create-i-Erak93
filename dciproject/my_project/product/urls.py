from django.contrib import admin
from django.urls import path, include #new
from product import views
from rest_framework.authtoken.views import obtain_auth_token


app_name='product'

urlpatterns = [
    
    path('',views.index,name="index"),
    path('/list',views.ProductList.as_view(),name="product_list"),
    path('/<int:pk>/',views.ProductDetail.as_view(),name="product_detail"),
    path('/update/<int:pk>/',views.ProductUpdate.as_view(),name="product_update"),
    path('/delete/<int:pk>/',views.ProductDelete.as_view(),name="product_delete"),
]



