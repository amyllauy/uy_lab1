from django.contrib import admin

from .models import User, Key, Nickname, Bio, Week

# Register your models here.
admin.site.register(User)
admin.site.register(Nickname)
admin.site.register(Bio)
admin.site.register(Key)
admin.site.register(Week)