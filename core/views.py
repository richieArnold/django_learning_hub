from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Course
#  import User model from django.contrib.auth.models
from django.contrib.auth.models import User
# authentication login
from django.contrib.auth import authenticate, login , logout
# login required decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    # if user is already logged in , redirect to viewCourses page
    if request.user.is_authenticated:
        # create a sesson timer and if the timer exceeds, then log the user out and redirect to home page
        return redirect("viewCourses")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        # if user is found, log them in and redirect to viewCourses page, otherwise return an error message
        if user is not None:
            login(request, user)
            return redirect("viewCourses")
        else:
            return render(request, "core/home.html", {"error": "Invalid username or password"})
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return HttpResponse("This is the contact page.")

def blogs(request):
    return HttpResponse("This is the blogs page.")

@login_required
def addCourse(request):
    # render the form
    if request.method == "POST":
        # get the form data
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")
        thumbnail = request.FILES.get("thumbnail")
        # create a new course object and save it to the database
        Course.objects.create(title=title, description=description, price=price, thumbnail=thumbnail)
        # return HttpResponse("Course added successfully.")
        return redirect("viewCourses")
    return render(request, "core/addCourse.html")

@login_required
def viewCourses(request):
    courses = Course.objects.all() # get all courses from the database
    # select * from courses
    # pass the courses to the template {"courses": courses}
    print(courses)
    return render(request, "core/viewCourses.html", {"courses": courses})

@login_required
def courseDetail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "core/viewCourse.html", {"course": course})

@login_required
def deleteCourse(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect("viewCourses")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # create a new user object and save it to the database
        # if username is already taken, return an error message
        if User.objects.filter(username=username).exists():
            return render(request, "core/register.html", {"error": "Username already taken"})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect("home")
    return render(request, "core/register.html")

def logout_view(request):
    # call a session timer and if the timer exceeds, then log the user out and redirect to home page
    logout(request)
    return redirect("home")