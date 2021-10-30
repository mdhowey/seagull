from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="home"),
    path('products/', views.ProductsList.as_view(), name="products_list"),
    path('products/new/', views.ProductCreate.as_view(), name="product_create"),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name="product_detail"),
    path('products/<int:pk>/update', views.ProductUpdate.as_view(), name="product_update"),
    path('products/<int:pk>/delete', views.ProductDelete.as_view(), name="product_delete"),
]