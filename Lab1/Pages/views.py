from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import UserForm, NicknameForm, BioForm, KeyForm, WeekForm, TodayForm
from .models import User, Nickname, Bio, Key, Week, Today

# Create your views here.
def redir_view(request):
	response = redirect("/home")
	return response

def home_view(request, *args, **kwargs):
	user=User.objects.first()
	if user==None:
		form=UserForm(request.POST or None)
		if form.is_valid():
			form.save()
		context = {"form": form, "message": "Hello! What is your name?"}
		return render(request, "home.html", context)
	else:
		context={"name": user}
		return render(request, "home2.html", context)



def profile_view(request, *args, **kwargs):
	if Nickname.objects.last()==None:
		nickname = "Your Nickname"
	else:
		nickname = Nickname.objects.last()
	if Bio.objects.last()==None:
		bio = "A short description about yourself."
	else:
		bio = Bio.objects.last()

	context = {"nickname": nickname, "bio": bio}
	return render(request, "profile.html", context)

def edit_nickname_view(request, *args, **kwargs):
	form=NicknameForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("/profile")
	return render(request, "edit_nickname.html", {"form": form})

	task = Week.objects.get(pk=pk)

def edit_bio_view(request, *args, **kwargs):	
	form=BioForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("/profile")
	return render(request, "edit_bio.html", {"form": form})



def key_view(request, *args, **kwargs):
	keyList=Key.objects.all()
	return render(request, "key.html", {"KeyList": keyList})

def add_key_view(request, *args, **kwargs):
	form=KeyForm(request.POST or None)
	if form.is_valid():
		form.save()
	return render(request, "add_key.html", {"form": form})



def week_view(request, *args, **kwargs):
	weekList=Week.objects.all()
	return render(request, "this_week.html", {"WeekList": weekList})

def add_week_view(request, *args, **kwargs):
	form=WeekForm(request.GET)

	form=WeekForm(request.POST or None)
	if form.is_valid():
		form.save()
	return render(request, "add_week.html", {"form": form})

def edit_week_view(request, pk):
	task = Week.objects.get(pk=pk)

	form=WeekForm(request.POST or None, instance=task)
	if request.method == "POST":
		
		if form.is_valid():
			form.save()
			return redirect("/this_week")
	return render(request, "edit_week.html", {"form" : form} )

def delete_week_view(request, pk):
	task = Week.objects.get(pk=pk)

	if request.method == "POST":
		task.delete()
		return redirect("/this_week")
	return render(request, "delete_week.html", {"task": task} )

def mark_week_view(request, pk):
	return render(request, "delete_week.html", {"task": task} )



def today_view(request, *args, **kwargs):
	todayList=Today.objects.all()
	return render(request, "today.html", {"TodayList": todayList})

def add_today_view(request, *args, **kwargs):
	form=TodayForm(request.GET)

	form=TodayForm(request.POST or None)
	if form.is_valid():
		form.save()
	return render(request, "add_today.html", {"form": form})

def edit_today_view(request, pk):
	task = Today.objects.get(pk=pk)

	form=TodayForm(request.POST or None, instance=task)
	if request.method == "POST":
		
		if form.is_valid():
			form.save()
			return redirect("/today")
	return render(request, "edit_today.html", {"form" : form} )


def delete_today_view(request, pk):
	task = Today.objects.get(pk=pk)

	if request.method == "POST":
		task.delete()
		return redirect("/today")
	return render(request, "delete_today.html", {"task": task} )

def mark_today_view(request, pk):
	return render(request, "delete_today.html", {"task": task} )