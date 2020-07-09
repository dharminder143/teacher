from django.contrib import admin
from  . models import *
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group

class userAdmin(admin.ModelAdmin):
	model = User
	list_display = ['groups_id','groups','username',]

admin.site.register(User,userAdmin)

# class GroupAdmin(admin.ModelAdmin):
# 	model = Group
# 	list_display = ['groups__id']

admin.site.register(Skill_level)