from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def redir_view(request):
	response = redirect("/home")
	return response

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def profile_view(request, *args, **kwargs):
	return render(request, "profile.html", {})

def key_view(request, *args, **kwargs):
	return render(request, "key.html", {})

def week_view(request, *args, **kwargs):
	return render(request, "this_week.html", {})

def today_view(request, *args, **kwargs):
	return render(request, "today.html", {})
