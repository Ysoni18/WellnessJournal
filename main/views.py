from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import class_id, teacher_id
from .forms import text
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import logout
from datetime import datetime

def home(request):
	try:
		
		user = list(request.user.groups.filter(name='student'))
		t_user = list(request.user.groups.filter(name='teacher'))
		if t_user:
			role = 'teacher'
			template = loader.get_template('main/class.html')
		
			
			for ids in teacher_id.objects.all():
					
				if str(ids.user) == str(request.user.username):
					code = ids.number
					break
				else:
					continue
			
			queries = class_id.objects.all()
			context = {
				'queries': queries,
				'code': code,
			}
			return HttpResponse(template.render(context, request))

			
		if user:
			
			role = 'student'
			
			template = loader.get_template('main/journal.html')
			past = class_id.objects.all()
			
			if request.method == "POST":
				form = text(request.POST)
				

				if form.is_valid():
					
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
					print('')

			else:	
				
				form = text()

			context = {
				'past': past,
				'form': form
				}		
			return render(request, 'main/journal.html', context=context)
		return render(request, 'register/redirect.html')
	except:
		return render(request, 'register/redirect.html')
		
def logoutview(request):
	logout(request)
	return render(request,'register/redirect.html')




