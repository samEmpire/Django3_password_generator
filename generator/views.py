from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    upper=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    spec=list('@#$%&*')
    num=list('0123456789')

    if request.GET.get('uppercase'):
        characters.extend(upper)
    if request.GET.get('special'):
        characters.extend(spec)
    if request.GET.get('number'):
        characters.extend(num)
    thepassword=''

    length=int(request.GET.get('length','6'))
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')

def contact(request):
    return render(request,'generator/contact.html')