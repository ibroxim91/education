from django.shortcuts import render

# Create your views here.


def all_courses(request):
    courses = ["Python", "Java", "C++","Go","PHP"]
    data = {"kurslar": courses}
    return render(request, "courses.html", context=data)