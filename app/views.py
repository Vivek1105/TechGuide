import email
from unicodedata import decomposition, name
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from app.models import Contact


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def product(request):
    return render(request,'product.html')

def service(request):
    return render(request,'service.html')

# def contact(request):
#     return render(request,'contact.html')

def Hackathon(request):
    return render(request,'hackathons.html')

def google(request):
    return render(request,'google.html')

def amazon(request):
    return render(request,'amazon.html')

def adobe(request):
    return render(request,'adobe.html')

def intel(request):
    return render(request,'intel.html')



def contact(request):
    if request.method=="POST":
        name= request.POST['name'] 
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['desc']
        # print(name,email,phone,desc)
        contact = Contact(name= name, email=email,phone=phone,desc=desc)
        contact.save()
        print("the data has been written to the db suscessfully")


    return render(request, 'contact.html')
    # return HttpResponse("this is my contact page ")