from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):
    d = {"id":1,"name":"Olim","last_name":"Olimov","age":21,"phone":998991234567}
    return JsonResponse(d)

