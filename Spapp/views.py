from django.shortcuts import render, redirect
from .models import Contact_Us, Category, SignUp, Product, Address
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import math
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from .helper import send_forgot_password_mail
import uuid

# Create your views here.

def index(request):
    recent = Contact_Us.objects.all().order_by("-id")[:5]
    cats = Category.objects.all().order_by("cat_name")
    prod = Product.objects.all()
    return render(request, 'Spapp/home.html', {"messages": recent, "category": cats, "products": prod})

def about(request):
    cats = Category.objects.all().order_by("cat_name")
    return render(request, 'Spapp/about.html', {"category": cats})

def contact_page(request):
    cats = Category.objects.all().order_by("cat_name")
    return render(request, 'Spapp/contact.html', {"category": cats})

@csrf_exempt
def contact(request):
    name = request.POST.get('name')
    message = request.POST.get('message')
    contact = request.POST.get('contact')
    subject = request.POST.get('subject')

    if Contact_Us.objects.filter(name=name, contact_number = contact).exists():
        response = "alreadyexist"
    else:
        data = Contact_Us(name=name, contact_number=contact, subject=subject, message=message)
        data.save()
        print("Data is saved")
        response = "success"
    return HttpResponse(response)

def signup(request):
    cats = Category.objects.all().order_by("cat_name")
    return render(request, 'Spapp/signup.html', {"category": cats})

@csrf_exempt
def signup_ajax(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    contact = request.POST.get('contactid')
    image_file = request.FILES.get('image_file')

    if SignUp.objects.filter(username=username).exists():
        response = "alreadyexist"
    else:
        signupinfo = SignUp(first_name=first_name, last_name=last_name, username=username, password=password, email=email, contact_number=contact, profile_pic=image_file)
        signupinfo.save()

        # fss = FileSystemStorage()
        # file = fss.save(image_file.name, image_file)
        # file_url = fss.url(file)
        print("User is signup")
        response = "success"
    return HttpResponse(response)

@csrf_exempt
def login_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if SignUp.objects.filter(username=username, password=password).exists():
        request.session['user_id'] = SignUp.objects.get(username = username, password = password).id
        request.session['Username'] = username
        pic = SignUp.objects.get(username = username, password = password)
        request.session['Profile_pic'] = pic.profile_pic.url
        print(pic.profile_pic.url)
        response = "success"
    else:
        response = "invalid"
    return HttpResponse(response)

def dashboard_page(request):
    allProds = []
    catprods = Product.objects.values('prod_category', 'id')
    cats = {item['prod_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(prod_category=cat)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    img = SignUp.objects.all()
    params = {'allProds':allProds, 'img':img}

    return render(request, 'Spapp/dashboard_page.html', params)

def user_logout(request):
    try:
        del request.session['Username']
    except KeyError:
        pass
    return redirect('home')

@csrf_exempt
def forgot_password_ajax(request):
    emailmodal = request.POST.get('emailmodal')
    if SignUp.objects.filter(email= emailmodal).exists():
        emailID_obj = SignUp.objects.get(email = emailmodal)
        token = str(uuid.uuid4())
        email = emailID_obj.email
        emailID_obj.forgot_password_token = token
        emailID_obj.save()

        print("EMAIL", email)
        send_forgot_password_mail(email, token)
        response = "success"
    else:
        response = "error"
    return HttpResponse(response)

@csrf_exempt
def forgot_change_password(request, token):
    context = {}
    try:
        user_obj = SignUp.objects.filter(forgot_password_token = token).first()
        print(user_obj)
        context = {'user_id': user_obj.id}
    except Exception as e:
        raise
    return render(request, 'Spapp/forgot_change_password.html', context)

@csrf_exempt
def forgot_change_password_ajax(request):
    if request.method == 'POST':
        passid1 = request.POST.get('passid1')
        passid2 = request.POST.get('passid2')
        user_id = request.POST.get('user_id')
        user_obj = SignUp.objects.get(id=user_id)
        user_obj.password = passid1
        user_obj.save()
        response="success"
    else:
        response="error"
    return HttpResponse(response)

def productview(request, id):
    #Fetch the product using id
    product = Product.objects.filter(id=id)
    print(product)
    print("In product view")
    return render(request, 'Spapp/productview.html', {'product': product[0]})

def checkout(request):
    signup_user_obj = SignUp.objects.all()
    return render(request, 'Spapp/checkout.html', {'signup_user_obj': signup_user_obj})

@csrf_exempt
def place_order_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        phone = request.POST.get('phone')
        save_data = Address(name=name, email=email, Address1=address1, Address2=address2, city=city, state=state, zip=zip, Phone_no=phone)
        save_data.save()
        print("record save..")
        response="success"
    else:
        response="error"
    return HttpResponse(response)
