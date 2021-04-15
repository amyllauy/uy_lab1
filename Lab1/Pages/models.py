from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Nickname(models.Model):
	nickname = models.CharField(max_length=50)

	def __str__(self):
		return self.nickname

class Bio(models.Model):
	bio = models.TextField()

	def __str__(self):
		return self.bio

class Key(models.Model):
	keyName = models.CharField(max_length=50)
	keyDesc = models.CharField(max_length=100)

	def __str__(self):
		keyName = self.keyName
		keyDesc = self.keyDesc
		fullEntry =  keyName +" ("+ keyDesc+")"
		return fullEntry

class Week(models.Model):
	weekKey = models.ForeignKey(Key, on_delete=models.SET_NULL, null=True)
	weekDesc = models.CharField(max_length=100)
	weekDone = models.BooleanField(default=False)

	def __str__(self):
		weekKey = self.weekKey
		weekDesc = self.weekDesc
		fullEntry =  weekKey.__str__() + " - " + weekDesc
		return fullEntry

class Today(models.Model):
	todayKey = models.ForeignKey(Key, on_delete=models.SET_NULL, null=True)
	todayDesc = models.CharField(max_length=100)
	todayDone = models.BooleanField(default=False)

	def __str__(self):
		todayKey = self.todayKey
		todayDesc = self.todayDesc
		fullEntry =  todayKey.__str__() + " - " + todayDesc
		return fullEntry