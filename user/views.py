from django.shortcuts import render,HttpResponse,redirect
from .models import emo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.shortcuts import HttpResponseRedirect



def first(request):
	return render(request,"first.html")

def happy(request):
	return render(request,"happy.html")

def sad(request):
	return render(request,"sad.html")

def suprise(request):
	return render(request,"suprise.html")

def fear(request):
	return render(request,"fear.html")

def angry(request):
	return render(request,"angry.html")

def confused(request):
	return render(request,"confused.html")

def login(request):
	return render(request,"index.html")


def login_user(request):
	username = request.POST['uname']
	password = request.POST['passwd']
	request.session['username'] = username
	print(username+" "+password)


	user = emo.objects.get(uname=username)
	
	if user.passwd==password:
		context = {'login':True}
		return render(request,"first.html",context)
	else:
		message = 'Login Failed'
		
	context = {
		'message' : message
	}
	return render(request,"index.html",context)
	


def signup(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			auth_login(request, user)
			return redirect('/user/')
		else:
			return render(request, 'signup.html', {'form': form})
	else:
		form = UserCreationForm()
		return render(request, "signup.html",{'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'first.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/user/') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def profile(request): 
    return render(request, 'profile.html') 

def signout(request):
    logout(request)
    return redirect('/user/')

def source(request):

	
	print(request.POST)
	if request.POST.get("HS1.x"):
		print("HW1 was clicked")
		request.session['EU']="1F600"
	elif request.POST.get("HS2.x"):
		print("HW2 was clicked")
		request.session['EU']="1F607"	
	elif request.POST.get("HS3.x"):
		print("HW3 was clicked")
		request.session['EU']="1F60E"
	elif request.POST.get("HS4.x"):
		print("HM1 was clicked")
		request.session['EU']="1F60C"
	elif request.POST.get("HS5.x"):
		print("HM2 was clicked")
		request.session['EU']="1F61D"
	elif request.POST.get("HS6.x"):
		print("HM3 was clicked")
		request.session['EU']="1F619"
	elif request.POST.get("HS7.x"):
		print("HS1 was clicked")
		request.session['EU']="1F606"
	elif request.POST.get("HS8.x"):
		print("HS2 was clicked")
		request.session['EU']="1F602"
	elif request.POST.get("HS9.x"):
		print("HS3 was clicked")
		request.session['EU']="263A"
	
	elif request.POST.get("FW1.x"):
		request.session['EU']="1F62C"
	elif request.POST.get("FW2.x"):
		request.session['EU']="1F637"
	elif request.POST.get("FW3.x"):
		request.session['EU']="1F622"
	elif request.POST.get("FM1.x"):
		request.session['EU']="1F616"
	elif request.POST.get("FM2.x"):
		request.session['EU']="1F633"
	elif request.POST.get("FM3.x"):
		request.session['EU']="1F61F"
	elif request.POST.get("FS1.x"):
		request.session['EU']="1F630"
	elif request.POST.get("FS2.x"):
		request.session['EU']="1F631"
	elif request.POST.get("FS3.x"):
		request.session['EU']="1F628"
	
	elif request.POST.get("SW1.x"):
		request.session['EU']="1F615"
	elif request.POST.get("SW2.x"):
		request.session['EU']="1F612"
	elif request.POST.get("SW3.x"):
		request.session['EU']="1F616"
	elif request.POST.get("SM1.x"):
		request.session['EU']="1F62B"
	elif request.POST.get("SM2.x"):
		request.session['EU']="1F623"
	elif request.POST.get("SM3.x"):
		request.session['EU']="1F625"
	elif request.POST.get("SS1.x"):
		request.session['EU']="1F61E"
	elif request.POST.get("SS2.x"):
		request.session['EU']="1F62D"
	elif request.POST.get("SS3.x"):
		request.session['EU']="1F622"
	
	elif request.POST.get("SUW1.x"):
		request.session['EU']="1F636"
	elif request.POST.get("SUW2.x"):
		request.session['EU']="1F611"
	elif request.POST.get("SUW3.x"):
		request.session['EU']="1F614"
	elif request.POST.get("SUM1.x"):
		request.session['EU']="1F610"
	elif request.POST.get("SUM2.x"):
		request.session['EU']="1F603"
	elif request.POST.get("SUM3.x"):
		request.session['EU']="1F60A"
	elif request.POST.get("SUS1.x"):
		request.session['EU']="1F633"
	elif request.POST.get("SUS2.x"):
		request.session['EU']="1F60D"
	elif request.POST.get("SUS3.x"):
		request.session['EU']="1F631"

	elif request.POST.get("DW1.x"):
		request.session['EU']="1F61E"
	elif request.POST.get("DW2.x"):
		request.session['EU']="1F637"
	elif request.POST.get("DW3.x"):
		request.session['EU']="1F621"
	elif request.POST.get("DM1.x"):
		request.session['EU']="1F620"
	elif request.POST.get("DM2.x"):
		request.session['EU']="1F62B"
	elif request.POST.get("DM3.x"):
		request.session['EU']="1F612"
	elif request.POST.get("DS1.x"):
		request.session['EU']="1F624"
	elif request.POST.get("DS2.x"):
		request.session['EU']="1F616"
	elif request.POST.get("DS3.x"):
		request.session['EU']="1F623"

	elif request.POST.get("AW1.x"):
		request.session['EU']="1F61F"
	elif request.POST.get("AW2.x"):
		request.session['EU']="1F611"
	elif request.POST.get("AW3.x"):
		request.session['EU']="1F623"
	elif request.POST.get("AM1.x"):
		request.session['EU']="1F618"
	elif request.POST.get("AM2.x"):
		request.session['EU']="1F62B"
	elif request.POST.get("AM3.x"):
		request.session['EU']="1F612"
	elif request.POST.get("AS1.x"):
		request.session['EU']="1F624"
	elif request.POST.get("AS2.x"):
		request.session['EU']="1F621"
	elif request.POST.get("AS3.x"):
		request.session['EU']="1F620"

	if request.POST.get("HS1.x") or request.POST.get("HS2.x") or request.POST.get("HS3.x") or request.POST.get("HS4.x") or request.POST.get("HS5.x") or request.POST.get("HS6.x") or request.POST.get("HS7.x") or request.POST.get("HS8.x") or request.POST.get("HS9.x"):
		request.session['emo']="0"
	elif request.POST.get("FW1.x") or request.POST.get("FW2.x") or request.POST.get("FW3.x") or request.POST.get("FM1.x") or request.POST.get("FM2.x") or request.POST.get("FM3.x") or request.POST.get("FS1.x") or request.POST.get("FS2.x") or request.POST.get("FS3.x"):
		request.session['emo']="1"
	elif request.POST.get("SW1.x") or request.POST.get("SW2.x") or request.POST.get("SW3.x") or request.POST.get("SM1.x") or request.POST.get("SM2.x") or request.POST.get("SM3.x") or request.POST.get("SS1.x") or request.POST.get("SS2.x") or request.POST.get("SS3.x"):
		request.session['emo']="2"
	elif request.POST.get("SUW1.x") or request.POST.get("SUW2.x") or request.POST.get("SUW3.x") or request.POST.get("SUM1.x") or request.POST.get("SUM2.x") or request.POST.get("SUM3.x") or request.POST.get("SUS1.x") or request.POST.get("SUS2.x") or request.POST.get("SUS3.x"):
		request.session['emo']="3"
	elif request.POST.get("DW1.x") or request.POST.get("DW2.x") or request.POST.get("DW3.x") or request.POST.get("DM1.x") or request.POST.get("DM2.x") or request.POST.get("DM3.x") or request.POST.get("DS1.x") or request.POST.get("DS2.x") or request.POST.get("DS3.x"):
		request.session['emo']="4"
	else :
		request.session['emo']="5"

	return render(request,'source.html')


def thankyou(request):
	ob=emo()
	username = request.user
	ob.uname=username 
	ob.emotion=request.session['emo']
	ob.EU=request.session['EU']
	
	if request.POST.get("HSi.x"):
		print("internal")
		ob.source=0
		
	elif request.POST.get("HSe.x"):
		
		print("external")
		ob.source=1

	ob.save()
	return render(request,'thankyou.html')

