from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hii")

# after creating index.html in templates
def home(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())