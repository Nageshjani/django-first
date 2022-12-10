from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def hello(request):
    dic={'name':'Nagesh'}
    return render(request,'index.html',dic)


def image(request):
    return render(request,'image.html')

def css(request):
    return render(request,'csss.html')

