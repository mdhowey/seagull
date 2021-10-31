from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
# class UserManager(BaseUserManager):
    
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email = self.normalize_email(email)
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_staffuser(self, email, password):
        
#         user = self.create_user(
#             email,
#             password=password
#         )

#         user.staff = True
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, password):
        
#         user = self.create_user(
#             email,
#             password=password
#         )

#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):

#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     is_active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)
#     models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def get_full_name(self):
#         return self.email # User is id'd by email

#     def get_short_name(self):
#         return self.email # User is id'd by email

#     def __str__(self): 
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         return True # Needs to be changed; just for testing

#     def has_module_perms(self, app_label):
#         "Does the user have persmissions to view the app?" #`app_label`
#         return True # Needs to be changed; just for testing

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.staff

#     @property
#     def is_admin(self):
#         "Is this user admin?"
#         return self.admin

#     objects = UserManager()


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']