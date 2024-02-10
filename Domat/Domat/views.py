from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def home(request):
    return render(request,'Main.html')

def login(request):
    return render(request,'login.html')

def register(request):
    # try:
    #     if request.method == "POST":
    #         email = request.POST.get('email')
    #         password = request.POST.get('password')
    #         first_name = request.POST.get('fname')
    #         last_name = request.POST.get('lname')

    #         new_user = User.objects.create(email,password)
    #         new_user.first_name = first_name
    #         new_user.last_name = last_name
    #         new_user.save()

    #         messages.success(request, "Your account has been created")

    #         return render(request,'login.html')
    # except:
        return render(request,'register.html')

def termsandcondition(request):
    return render(request,'t&c.html')

def shop(request):
    return render(request,'shop.html')

def clothing(request):
    return render(request,'clothing.html')

def shoes(request):
    return render(request,'shoes.html')

def accessories(request):
    return render(request,'accessories.html')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Skip saving the form data
            print("Registration successful. Redirecting to success_page.")
            return redirect('success_page')
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
def success_page(request):
    return render(request, 'success_page.html')