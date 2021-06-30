from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages 
from .forms import NewUserForm
# Create your views here.

def single_slug(request,single_slug):
	categories = [c.category_slug for c in TutorialCategory.objects.all()]
	if single_slug in categories:
		mathcing_series = TutorialSeries.objects.filter(tutorial_category__category_slug= single_slug)

		series_url = {}
		for m in mathcing_series.all():
			part_one = Tutorial.objects.filter(tutorial_series__tutorial_series = m.tutorial_series).earliest("tutorial_published")
			print(part_one)
			series_url[m] = part_one.tutorial_title

		return render(request,
					  "main/category.html",
					  {"part_ones" : series_url})

	tutorials = [t.tutorial_title for t in Tutorial.objects.all()]
	if single_slug in tutorials:
		this_tutorial = Tutorial.objects.get(tutorial_title = single_slug)
		tutorials_from_series = Tutorial.objects.filter(tutorial_series = this_tutorial.tutorial_series).order_by("tutorial_published")
		#why not double underscore ?? because this_tutorial is same object as Tutorial
		return render(request,
					  "main/tutorial.html",
					  {"tutorial" : this_tutorial,
					   "sidebar" :tutorials_from_series})


	return HttpResponse(f"{single_slug} doesn't correspond to anything!!!")

def homepage(request):

	#return HttpResponse("Wow this is an <strong>awesome</strong> tutorial")

	return render(request=request,
				  template_name= "main/categories.html",
				  context= {"categories" : TutorialCategory.objects.all })


def register(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New User Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as: {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg} : {form.error_messages[msg]}")


	form = NewUserForm
	context = {'form' : form}
	return render(request, 'main/register.html', context)


def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("/") #return redirect("main:homepage")

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username,password= password)
			if user:
				login(request, user)
				messages.info(request, f"You are now logged in as: {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, f"Invalid username or password")	
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg} : {form.error_messages[msg]}")

	form = AuthenticationForm
	return render(request, 'main/login.html', {'form':form})
