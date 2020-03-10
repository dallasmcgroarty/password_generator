from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # returning a template from generator and also a dict with a password key
    # by returning a dict, the template file in this example is home.html
    # home.html can access the value of password by using {{ password }}
    # in the html file, and it will output it to the html page
    return render(request, 'generator/home.html', {'password':'fkj243f24'})