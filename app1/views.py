from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import StudentModel
from django.db.models import Q

# Create your views here.

#Home page
@login_required(login_url='login') 
def home_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added Successfully")
            return redirect('home')
    else:
        form = StudentForm()  
    return render(request, 'home.html',{"form": form})


@login_required
def all_student_view(request):
    query = request.GET.get('search', '')
    if query:
        students = StudentModel.objects.filter(
            Q(fname__icontains=query)|
            Q(lname__icontains=query)|
            Q(email__icontains=query)
        )
    else:    
        students = StudentModel.objects.all()
    return render(request, 'all_students.html', context={"students": students})

def edit_view(request, id):
    student = get_object_or_404(StudentModel, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('allStudent')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', context={"form": form})    

def delete_view(request, id):
    student = get_object_or_404(StudentModel, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('allStudent') 

    return render(request, 'delete_student.html', context={"student": student})   

#login_page
def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')        

def signup_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        messages.success(request, "Account created successfully!")
        login(request, user)
        return redirect('signup')
    return render(request,'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')