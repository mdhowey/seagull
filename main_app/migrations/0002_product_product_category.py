# Generated by Django 3.2.8 on 2021-10-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('General', 'General'), ('Appliances', 'Appliances'), ('Auto & Tire', 'Auto & Tire'), ('Baby & Toddler', 'Baby & Toddler'), ('Cigarettes & Tabacco', 'Cigarettes & Tabacco'), ('Clothing', 'Clothing'), ('Jewlery', 'Jewlery'), ('Shoes', 'Shoes'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Home Goods', 'Home Goods'), ('Office', 'Office'), ('Sports', 'Sports')], default='General', max_length=255),
        ),
    ]
