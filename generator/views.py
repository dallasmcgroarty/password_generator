from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
# form data stored in request variable

def home(request):
    # returning a template from generator and also a dict with a password key
    # by returning a dict, the template file in this example is home.html
    # home.html can access the value of password by using {{ password }}
    # in the html file, and it will output it to the html page
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-+_[]?'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for _ in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')