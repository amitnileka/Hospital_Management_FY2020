from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.utils import timezone
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
			if user.is_staff:
				login(request,user)
				print("Succesful")
				return redirect('adminhome')
			elif user is not None:
				login(request,user)
				error = "no"
				g = request.user.groups.all()[0].name
				if g == 'Doctor':
					return redirect('patientdash')
				elif g == 'Patient':
					return redirect('patientdash')
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

def logoutpg(request):
	logout(request)
	return redirect('login')

def patientinfo(request):
	if not request.user.is_active:
		return redirect('login')
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		patient_details=Patient.objects.all().filter(username=request.user)
		d={'patient_details':patient_details}
		return render(request,'patientinfo.html',d)
	elif g== 'Doctor':
		doctor_details=Doctor.objects.all().filter(username=request.user)
		d={'doctor_details':doctor_details}
		return render(request,'doctorinfo.html',d)

	
	

def patientdash(request):
	if not request.user.is_active:
		return redirect('login')
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		patient_details=Patient.objects.all().filter(username=request.user)
		d={'patient_details':patient_details}
		return render(request,'patientdash.html',d)
	elif g== 'Doctor':
		doctor_details=Doctor.objects.all().filter(username=request.user)
		d={'doctor_details':doctor_details}
		return render(request,'doctorhome.html',d)
	
def patientprofile(request):
	
	
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		patient_details=Patient.objects.all().filter(username=request.user)
		d={'patient_details':patient_details}
		return render(request,'patientprofile.html',d)
	elif g== 'Doctor':
		doctor_details=Doctor.objects.all().filter(username=request.user)
		d={'doctor_details':doctor_details}
		return render(request,'doctorprofile.html',d)


def MakeAppointments(request):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	alldoctors = Doctor.objects.all()
	d = { 'alldoctors' : alldoctors }
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		if request.method == 'POST':
			doctoremail = request.POST['doctoremail']
			doctorname = request.POST['doctorname']
			username = request.POST['username']
			patientemail = request.POST['patientemail']
			appointmentdate = request.POST['appointmentdate']
			appointmenttime = request.POST['appointmenttime']
			symptoms = request.POST['symptoms']
			try:
				Appointment.objects.create(doctorname=doctorname,doctoremail=doctoremail,username=username,patientemail=patientemail,appointmentdate=appointmentdate,appointmenttime=appointmenttime,symptoms=symptoms,status=True,prescription="")
				error = "no"
			except:
				error = "yes"
			patient_details=Patient.objects.all().filter(username=request.user)
			e = {"error":error,"patient_details":patient_details}
			
			return render(request,'patientmakeappointments.html',e)
		elif request.method == 'GET':
			return render(request,'patientmakeappointments.html',d)

def viewappointments(request):
	if not request.user.is_active:
		return redirect('loginpage')
	#print(request.user)
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		u=Appointment.objects.all().filter(username=request.user)
		st={
			"stu":u
		}
		return render(request,'patientviewappointments.html',st)
	elif g== 'Doctor':
		pass


def temp(request):
	pd=Patient.objects.all().count()
	dd=Doctor.objects.all().count()
	gt={ "pd": pd,"dd":dd}
	return render(request,'temp.html',gt)

def patient_delete_appointment(request,pid):
	if not request.user.is_active:
		return redirect('login')
	appointment = Appointment.objects.get(id=pid)
	appointment.delete()
	return redirect('viewappointments')

def adminhome(request):
	if not  request.user.is_staff:
		return redirect('login')

	return render(request,'adminDash.html')


def adminaddpatient(request):
	if not  request.user.is_staff:
		return redirect('login')

	return render(request,'adminaddpatient.html')


def adminviewpatient(request):
	if not request.user.is_staff:
		return redirect('login')

	return render(request,'adminviewpatient.html')


def adminadddoctor(request):
	error = ""
	user="none"
	if not request.user.is_staff:
		return redirect('login')

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		username=request.POST['username']
		password = request.POST['password']
		repeatpassword =  request.POST['repassword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		address = request.POST['address']
		birthdate = request.POST['birthdate']
		bloodgroup = request.POST['bloodgroup']
		specialization = request.POST['specialization']
		
		try:
			if password == repeatpassword:
				Doctor.objects.create(name=name,email=email,password=password,gender=gender,username=username,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup,specialization=specialization)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=username)
				doc_group = Group.objects.get(name='Doctor')
				doc_group.user_set.add(user)
				user.save()
				error = "no"
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
			print(e)
	d = {'error' : error}
	return render(request,'adminadddoctor.html',d)


def adminviewdoctor(request):
	if not  request.user.is_staff:
		return redirect('login')

	return render(request,'adminviewdoctor.html')
