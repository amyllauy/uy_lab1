from django import forms

from .models import User, Nickname, Bio, Key, Week, Today

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["name"]

class NicknameForm(forms.ModelForm):
	class Meta:
		model = Nickname
		fields = ["nickname"]

class BioForm(forms.ModelForm):
	class Meta:
		model = Bio
		fields = ["bio"]

class KeyForm(forms.ModelForm):
	class Meta:
		model = Key
		fields = ["keyName", "keyDesc"]

class WeekForm(forms.ModelForm):
	class Meta:
		model = Week
		fields = ["weekKey", "weekDesc"]

class TodayForm(forms.ModelForm):
	class Meta:
		model = Today
		fields = ["todayKey", "todayDesc"]