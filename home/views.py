from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	# return HttpResponse('ini home')
	# return HttpResponse('<h1>sini la home</h1>')
	return render(request, 'home/home.html')