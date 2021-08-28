#I have created this file
# https://docs.djangoproject.com/en/3.2/intro/tutorial01/   documentation link

from django.http import HttpResponse

def index(request):   #it will take default argument which is called request
    return HttpResponse("Hello How are you gaurav...")


def about(request):
    return HttpResponse("<h1>Hello How are you kumar gaurav</h1>")

def contact(request):
    return HttpResponse("<h1>I Love You Payal</h1>")