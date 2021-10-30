from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField

# Create your models here.
class Product(models.Model):

    GENERAL = 'General'
    APPLIANCES = 'Appliances' 
    AUTOTIRE = 'Auto & Tire'
    BABYTODDLER = 'Baby & Toddler'
    CIGSTOBACCO = 'Cigarettes & Tabacco'
    CLOTHING = 'Clothing'
    JEWLERY = 'Jewlery'
    SHOES = 'Shoes'
    ELECTRONICS = 'Electronics'
    FURNITURE = 'Furniture'
    HOMEGOODS = 'Home Goods'
    OFFICE = 'Office'
    SPORTS = 'Sports'

    CATEGORIES = (
        (GENERAL, 'General'),
        (APPLIANCES, 'Appliances'), 
        (AUTOTIRE, 'Auto & Tire'),
        (BABYTODDLER, 'Baby & Toddler'),
        (CIGSTOBACCO, 'Cigarettes & Tabacco'),
        (CLOTHING, 'Clothing'),
        (JEWLERY, 'Jewlery'),
        (SHOES, 'Shoes'),
        (ELECTRONICS, 'Electronics'),
        (FURNITURE, 'Furniture'),
        (HOMEGOODS, 'Home Goods'),
        (OFFICE, 'Office'),
        (SPORTS, 'Sports'),
    )

    name = models.CharField(max_length=50, unique=True, null=False)
    img = models.CharField(max_length=250, default="https://www.legalgraphicworks.com/wp-content/plugins/bb-plugin/img/no-image.png")
    price = models.IntegerField(default=0)
    category = models.TextField(max_length=150, choices=CATEGORIES, default=GENERAL)
    description = models.TextField(max_length=500)