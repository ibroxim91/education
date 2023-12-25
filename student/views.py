from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from  .sendMail import send_user_mail
from course.models import Course , Category , Gallery
from django.contrib.auth.views import LoginView

from django.contrib.auth.models import User
from django.contrib import messages
from threading import Thread
from django.views.generic import TemplateView, ListView ,CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views import View


# Create your views here.

class  TestView(View):
    template_name = 'test.html'

    def get(self, request):
        context = {}
        context["categories"] = Category.objects.all()
        return render(request, self.template_name, context)

    def post(self, request):
        print()
        print(request.POST)
        print(request.user)
        print()
        title = request.POST.get('title')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id= int(category_id)  )
        author = User.objects.get(id=1)
        course = Course.objects.create(category=category, title=title, duration=duration,
                                       price=price, author=author)
        messages.add_message(request, messages.SUCCESS ,"Kurs qo'shilidi ")
        return redirect('/test')

    # # queryset = Course.objects.all()[:1]
    # context_object_name = "courses"  

    # def get_queryset(self) -> QuerySet[Any]:
    #     user = self.request.user
    #     queryset = Course.objects.filter(author=user)

    #     return  queryset






def home(request):
    print()
    print( request.user)
    print()
    # if  request.user.is_authenticated:
    #     return HttpResponseRedirect( reverse("student:login") )

    
    course_all = Course.objects.all()
    category_all = Category.objects.all()
    photos = Gallery.objects.all() 
    context = {"courses": course_all , "category_all":category_all ,"photos_all":photos}
    # return HttpResponseRedirect("https://uzum.uz")


    return render(request, "index.html", context)


def category_courses(request, id):
    c = Category.objects.get(id=id) #get_object_or_404( Category , id=id) 
    courses = Course.objects.filter(category=c)
    category_all = Category.objects.all()
    
    context = {"courses": courses,  "category_all":category_all }
    return render(request, "category.html", context)



class  MyLoginView(LoginView):
    pass
    # redirect_authenticated_user = "/"
    # template_name = "auth/login.html"



def register_view(request):
    if request.method == "POST":
  
        username =  request.POST.get('username')  
        email =  request.POST.get('email')  
        psw =  request.POST.get('psw')  
        psw_repeat =  request.POST.get('psw-repeat')

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.WARNING , "Bu username band !")
            return redirect("student:register")
        
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.WARNING , "Bu email band !")
            return redirect("student:register")
        
        if psw != psw_repeat:
            messages.add_message(request, messages.WARNING , "Parollar bir xil emas")
            return redirect("student:register")
        user = User.objects.create_user(username=username, email=email, password=psw)
        messages.add_message(request, messages.SUCCESS , "Ro'yxatdan o'tdingiz")
        Thread(target=send_user_mail , args=(email,) ).start()
        # send_user_mail(email)
        return redirect("student:login")

    return render(request, "registration/register.html")
