from django.contrib import admin
from Spapp.models import Student, Contact_Us, Category, SignUp, Product, Address

# Register your models here.
admin.site.site_header="My Website"

class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "roll_no", "fee", "gender", "address", "is_registered"]

class Contact_UsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "contact_number", "subject", "message", "added_on"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "cat_name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "prod_title"]

admin.site.register(Student, StudentAdmin)
admin.site.register(Contact_Us, Contact_UsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SignUp)
admin.site.register(Product, ProductAdmin)
admin.site.register(Address)
