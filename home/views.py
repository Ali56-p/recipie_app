from django.shortcuts import render
from django.http import HttpResponse
from django import template

# Create your views here.
def home(request):

    peoples = [
    {'name': 'Ali', 'age': 23},
    {'name': 'Alyan ', 'age': 93},
    {'name': 'Alia', 'age': 16},
    {'name': 'Alina', 'age': 43},
    {'name': 'Alishan', 'age': 13},

]
    
        
    
    
    # for people in peoples:
    #     print(people)


    return render (request, "index.html", context={'peoples': peoples })



