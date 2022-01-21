from django.db import models

# Create your models here.

class Student(models.Model):
    c =(
        ("M","Male"),("F","Female")
    )
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    roll_no = models.IntegerField(unique=True, null=True, blank=True)
    # date_of_birth = models.DateField(blank=True,default=None)
    fee = models.FloatField()
    gender = models.CharField(max_length=150,choices=c, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    is_registered = models.BooleanField()

    def __str__(self):
        return self.name+" "+str(self.roll_no)

    class Meta:
        verbose_name_plural= "Student"


class Contact_Us(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True,null=True)
    message = models.CharField(max_length=500, blank=True,null=True)
    added_on =models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"

class Category(models.Model):
    cat_name = models.CharField(max_length=250, null=True, blank=True)
    added_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = "Category of Product"

class SignUp(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200,  null=True, blank=True)
    username = models.CharField(max_length=250,  null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    contact_number = models.IntegerField(null=True, blank=True)
    forgot_password_token = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to ='uploads/', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Sign Up"

class Product(models.Model):
    prod_title = models.CharField(max_length=100, null=True, blank=True)
    prod_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    prod_desc = models.CharField(max_length=200, null=True, blank=True)
    prod_price = models.IntegerField(null=True, blank=True)
    prod_pic = models.FileField(upload_to="images/%y/%m/%d")

    def __str__(self):
        return self.prod_title

    class Meta:
        verbose_name_plural = "Product"

class Address(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    Address1 = models.CharField(max_length=100, null=True, blank=True)
    Address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    Phone_no = models.IntegerField(null=True, blank=True)
