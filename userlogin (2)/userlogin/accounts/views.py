from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse

def sems(request):
    return render(request, 'sems.html')

def addstudent(request):
    return render(request, 'addstudent.html')
def viewstudent(request):
    return render(request, 'viewstudent.html')
def updatestudent(request):
    return render(request, 'updatestudent.html')
def deletestudent(request):
    return render(request, 'deletestudent.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        User.objects.create(username=uname, email=email, password=pwd)
        messages.success(request, 'Registration successful.')
        return redirect('login')
    
    return render(request, 'register.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(email=email)
            user.password = make_password(new_password)
            user.save()
            messages.success(request, "Password reset successful. Please login.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "Email not found.")
    
    return render(request, 'forgot_password.html')


def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = request.session.get('user')  # assuming session-based login
        if user:
            current_user = User.objects.get(email=user)
            if check_password(old_password, current_user.password):
                if new_password == confirm_password:
                    current_user.password = make_password(new_password)
                    current_user.save()
                    messages.success(request, 'Password changed successfully.')
                    return redirect('login')
                else:
                    messages.error(request, 'New passwords do not match.')
            else:
                messages.error(request, 'Incorrect old password.')
        else:
            messages.error(request, 'You must be logged in.')
    return render(request, 'change_password.html')

def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        try:
            user = User.objects.get(username=uname, password=pwd)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('sems')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'login.html')


def user_logout(request):
    request.session.flush()
    return redirect('login')

def mca101(request):
   temp=loader.get_template('mca101.html')
   return HttpResponse(temp.render())
def mca102(request):
   temp=loader.get_template('mca102.html')
   return HttpResponse(temp.render())
def mca103(request):
   temp=loader.get_template('mca103.html')
   return HttpResponse(temp.render())

def mca104(request):
   temp=loader.get_template('mca104.html')
   return HttpResponse(temp.render())

def mca105(request):
   temp=loader.get_template('mca105.html')
   return HttpResponse(temp.render())

def mca106(request):
   temp=loader.get_template('mca106.html')
   return HttpResponse(temp.render())
def mca107(request):
   temp=loader.get_template('mca107.html')
   return HttpResponse(temp.render())
def mca108(request):
   temp=loader.get_template('mca108.html')
   return HttpResponse(temp.render())
def mca201(request):
   temp=loader.get_template('mca201.html')
   return HttpResponse(temp.render())
def mca202(request):
   temp=loader.get_template('mca202.html')
   return HttpResponse(temp.render())
def mca203(request):
   temp=loader.get_template('mca203.html')
   return HttpResponse(temp.render())
def mca204(request):
   temp=loader.get_template('mca204.html')
   return HttpResponse(temp.render())

def mca205(request):
   temp=loader.get_template('mca205.html')
   return HttpResponse(temp.render())

def mca206(request):
   temp=loader.get_template('mca206.html')
   return HttpResponse(temp.render())

def mca207(request):
   temp=loader.get_template('mca207.html')
   return HttpResponse(temp.render())
def mca208(request):
   temp=loader.get_template('mca208.html')
   return HttpResponse(temp.render())
def mca301(request):
   temp=loader.get_template('mca301.html')
   return HttpResponse(temp.render())
def mca302(request):
   temp=loader.get_template('mca302.html')
   return HttpResponse(temp.render())
def mca303(request):
   temp=loader.get_template('mca303.html')
   return HttpResponse(temp.render())
def mca304(request):
   temp=loader.get_template('mca304.html')
   return HttpResponse(temp.render())
def mca305(request):
   temp=loader.get_template('mca305.html')
   return HttpResponse(temp.render())

def mca306(request):
   temp=loader.get_template('mca306.html')
   return HttpResponse(temp.render())

def mca307(request):
   temp=loader.get_template('mca307.html')
   return HttpResponse(temp.render())

def mca308(request):
   temp=loader.get_template('mca308.html')
   return HttpResponse(temp.render())
def mca309(request):
   temp=loader.get_template('mca309.html')
   return HttpResponse(temp.render())

def mca401(request):
   temp=loader.get_template('mca401.html')
   return HttpResponse(temp.render())

def mca402(request):
   temp=loader.get_template('mca402.html')
   return HttpResponse(temp.render())
def mca403(request):
   temp=loader.get_template('mca403.html')
   return HttpResponse(temp.render())


def prabakar(request):
   temp=loader.get_template('prabakar.html')
   return HttpResponse(temp.render())

def murali(request):
   temp=loader.get_template('murali.html')
   return HttpResponse(temp.render())
def hasya(request):
   temp=loader.get_template('hasya.html')
   return HttpResponse(temp.render())

def chandra(request):
   temp=loader.get_template('chandra.html')
   return HttpResponse(temp.render())

def rushi(request):
   temp=loader.get_template('rushi.html')
   return HttpResponse(temp.render())
def praveen(request):
   temp=loader.get_template('praveen.html')
   return HttpResponse(temp.render())

# Create your views here.
