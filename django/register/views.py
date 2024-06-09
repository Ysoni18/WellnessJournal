from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, teacher_form
import random
from django.db import models
from django.contrib.auth.models import Group, User
from main.models import class_id, teacher_id


def find_role(request):
	return render(request, 'register/redirect.html', {})
def register(response):
	
	if response.method == 'POST':
		
		form = RegisterForm(response.POST)
		if form.is_valid():
			user = form.save()
			group = 'student'
			group_f = Group.objects.get(name=group)
			user_id = User.objects.get(username=user)
			group_f.user_set.add(user.id)
			
			return redirect('/login')
	else:
		form = RegisterForm()
	return render(response, 'register/register.html', {'form':form})
def teacher_register(request):
	if request.method == 'POST':
		form = teacher_form(request.POST)
		if form.is_valid():
			user_i = form.save()
			group = 'teacher'
			group_get = Group.objects.get(name=group)
			user_id = User.objects.get(username=user_i)
			group_get.user_set.add(user_i.id)
			class_code = random.randint(11111,32767)
			class_codes = teacher_id()
			class_codes.user = form.cleaned_data.get('username')
			class_codes.number = class_code
			print(class_code)
			class_codes.save()
			return redirect('/login')
		
	else:
		
		form = teacher_form()
	return render(request, 'register/teacher_register.html', {'form': form})

def logout(request):
	logout(request)
	return redirect(request, '/',{})