from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login  # Renamed for clarity
from .models import *  # Import all models (if necessary)


def intro(request):
    return render(request,"IntroPage.html")

def recruiter(request):
    return render(request,"recruiterSignIn.html")

def recru_dash(request):
    return render(request,"recruiter.html")
def admin(request):
    return render(request,"admin.html")
def homepage(request):
    return render(request, "home.html")

def login_view(request):  # Renamed to avoid conflict
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Signup.objects.filter(username=username).exists():
            if Signup.objects.filter(password=password).exists():
                return redirect('profile')
            else:
                return render(request,"login.html")
        else:
            return render(request,"login.html")
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        sigup=Signup(username=username,password=password)
        sigup.save()
        return redirect('registration')
    return render(request, "signup.html")


def registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        mid_name = request.POST['mid_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        branch = request.POST['branch']
        mail = request.POST['mail']
        cgpa = request.POST['cgpa']
        tenthmarks = request.POST['tenthmarks']
        twelfthmarks = request.POST['twelfthmarks']
        abcnumber = request.POST['abcnumber']


        try:
            # Create a new Registration object and save it
            new_registration = Registration(
                first_name=first_name,
                mid_name=mid_name,
                last_name=last_name,
                dob=dob,
                branch=branch,
                mail=mail,
                cgpa=cgpa,
                tenthmarks=tenthmarks,
                twelfthmarks=twelfthmarks,
                abcnumber=abcnumber,
            )
            new_registration.save()

            message = "Registration successful!"
            print(message)
            return redirect('home')  # Use the named URL for the homepage
        except Exception as e:  # Catch any exceptions during saving
            # Error message on encountering exceptions
            error_message = f"An error occurred: {e}"
            print(error_message)
            return render(request, "registration.html", {'error': error_message})

    return render(request, "registration.html")




def apply(request):
    return render(request,"apply.html")

def practice(request):
    return render(request,"pratice.html")

def profile(request):
    return render(request,"profile.html")

def jobs(request):
    return render(request,"jobs.html")
