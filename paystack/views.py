from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'home.html', context)

def checkout(request):
    #specifically for allowing user to subscribe
    #Do not allow user to go to the home page if they do not add their bank card

    return render(request, 'checkout.html')


def sign_up(request):
    #When the user is created, this view will redirect user to the checkout page, where user can add their card information
    if request.method == 'POST':
        username = request.POST['username']
        
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Or Username Already Taking')
                return redirect('Register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Taken')
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('Checkout')
        else:
            messages.info(request, 'Password Not Match')
            return redirect('Register') 

        return redirect ('/')     
    else:
        return render(request, 'signup.html')
