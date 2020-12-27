from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse
def index(request):
	return render(request,'homepage.html')

def about(request):
	return render(request,'about.html')
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def loginpage(request):
	
	if request.method == 'POST':
		u = request.POST['username']
		p = request.POST['password']
		user = authenticate(request,username=u,password=p)
		try:
			if user is not None:
				login(request,user)
				error = "no"
				g = request.user.groups.all()[0].name
				if g == 'Patient':
					page = "patient"
					d = {'error': error,'page':page}
					return render(request,'patientinfo.html',d)
			else:
				print('something is wrong')
				error = "yes"
				print(e)
		except Exception as e:
			error = "yes"
			print(e)
			#raise e
	return render(request,'login1.html')
def createAcc(request):
	error = ""
	user="none"
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repassword = request.POST.get('repassword')
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		username = request.POST['username']
		bloodgroup = request.POST['bloodgroup']
		try:
			if password == repassword:
				Patient.objects.create(name=name,email=email,username=username,password=password,repassword=repassword,gender=gender,phonenumber=phonenumber,bloodgroup=bloodgroup)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=username)
				pat_group = Group.objects.get(name='Patient')
				pat_group.user_set.add(user)
				#print(pat_group)
				user.save()
				#print(user)
				error = "no"
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
			#print("Error:",e)
	d = {'error' : error}
	#print(error)
	return render(request,'createAcc.html',d)
	#return render(request,'createaccount.html')
def contactus(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "contact.html")

def services(request):
	return render(request,'services.html')

def patientinfo(request):
	return render(request,'patientinfo.html')


