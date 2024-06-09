from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import class_id, teacher_id
from .forms import text
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth.models import User
import re
from datetime import datetime
#HALF OF THIS CODE ISN'T NEEDED, DELETE IT LATER
def journal(request):
	
		if user:
			role = 'student'
		elif t_user:
			role = 'teacher'
		context = {
		'user': role
		}
		class_ids = class_id.objects.all()
		form = text(request.POST)
		context = {
		'ids': class_ids
		}
		if request.method == "POST":
			if form.is_valid():

				
					tn = form.cleaned_data.get('text')
					ty = form.cleaned_data.get('class_id')
					
					t = class_id()
					t.number = ty
					t.text = tn
					t.save()
					
					return render(request, 'main/journal.html', context=context)
			else:
				
				form = text()
				return render(request,'main/journal.html',{'form':form}, context=context)
	
		return render(request, 'main/journal.html', {}, context=context)
		
		
	#return render(request, "main/journal.html", {"form":text})

def home(request):
	
		
		user = list(request.user.groups.filter(name='student'))
		t_user = list(request.user.groups.filter(name='teacher'))
		if t_user:
			role = 'teacher'
			template = loader.get_template('main/class.html')
		
			
			for ids in teacher_id.objects.all():
				print(ids.user)
				print(request.user.username)	
				if str(ids.user) == str(request.user.username):
					code = ids.number
					break
				else:
					continue
			print(code)
			queries = class_id.objects.all()
			context = {
				'queries': queries,
				'code': code,
			}
			return HttpResponse(template.render(context, request))

			
		if user:
			
			role = 'student'
			print(role)
			template = loader.get_template('main/journal.html')
			past = class_id.objects.all()
			
			if request.method == "POST":
				form = text(request.POST)
				

				if form.is_valid():
					print('yaay')
					title = form.cleaned_data.get('title')
					tex = form.cleaned_data.get('text')
					classid = form.cleaned_data.get('class_id')
					dates = datetime.now()

					t = class_id()
					t.title = title
					t.number = classid
					t.text = tex
					t.date = str(dates.strftime("%b") + ' ' + dates.strftime("%d"))
					t.user = request.user.username
					t.save()
					print('saved')
					context = {
					'past': past,
					'form': form
					}
					return render(request,'main/journal.html', context=context)
				else:
					print('nononoon')

			else:	
				
				form = text()

			context = {
				'past': past,
				'form': form
				}		
			return render(request, 'main/journal.html', context=context)
		else:			
			return render(request, 'main/main.html',{})
		
		

	

def Class(request):
	try:
		template = loader.get_template('main/class.html')
		user_s = list(request.user.groups.filter(name='student'))
		t_user = list(request.user.groups.filter(name='teacher'))
		if user_s:
			role = 'student'
		elif t_user:
			role = 'teacher'
		
		print(role)
		
		template = loader.get_template('main/class.html')
		
		print(request.user.username)
		for ids in teacher_id.objects.all():
			print(ids.user)
			print(ids)	
			if str(ids.user) == str(request.user.username):
				code = ids.number
				break
			else:
				continue
		print(code)
		queries = class_id.objects.all()
		context = {
			'queries': queries,
			'code': code,
		}

		
		return redirect(template.render(context, request))
	except:
		return redirect(request, 'register/redirect.html')


