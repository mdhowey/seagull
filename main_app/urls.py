from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="home"),
    path('products/', views.ProductsList.as_view(), name="products_list"),
]