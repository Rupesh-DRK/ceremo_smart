from django.shortcuts import render,redirect
import base64
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import *
from .context_processors import *
from .forms import pictureModelForm,UserProfileForm,historyModelForm,volunteerForm,GallerModelForm
from django.urls import reverse
from base64 import b64encode
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def pic(request):
    gallery=GalleryModel.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})

def home(request):
    return render(request,'index.html',{})

def events(request):
    session_id=request.session.get('_auth_user_id')
    if session_id:
        try:
            users = userData1.objects.get(pk=session_id)
            return render(request, 'events.html', {})
        except userData1.DoesNotExist:
            return redirect('userLogin')
    else:
        return render(request,'userLogin.html',{})
    


def contact(request):
    temp = loader.get_template('contact.html')
    return render(request,'contact.html',{})

def cradle(request):
    images = pictureModel.objects.all() 
    if request.method=='POST':
        form_name=request.POST['form_name']
        username=request.POST['username'] 
        email=request.POST['email'] 
        theme=request.POST['theme'] 
        cake=request.POST['cake'] 
        cradle=request.POST['cradle'] 
        entertainment=request.POST['entertainment'] 
        decoration=request.POST['decoration'] 
        balloons=request.POST['balloons'] 
        date=request.POST['date'] 
        guest=request.POST['guest']
        location=request.POST['location']
        m=HistoryModel()
        m.form_name=form_name
        m.username=username
        m.email=email
        m.theme=theme
        m.cake=cake
        m.cradle=cradle
        m.entertainment=entertainment
        m.decoration=decoration
        m.balloons=balloons
        m.date=date
        m.guest=guest
        m.location=location
        m.save()
        return redirect('my_bookings')
    return render(request, 'cradle.html', {'images': images})

def party(request):
    images = pictureModel.objects.all() 
    if request.method=='POST':
        form_name=request.POST['form_name']
        username=request.POST['username'] 
        email=request.POST['email'] 
        theme=request.POST['theme'] 
        cake=request.POST['cake'] 
        cradle=request.POST['cradle'] 
        entertainment=request.POST['entertainment'] 
        decoration=request.POST['decoration'] 
        balloons=request.POST['balloons'] 
        date=request.POST['date'] 
        guest=request.POST['guest']
        location=request.POST['location']
        m=HistoryModel()
        m.form_name=form_name
        m.username=username
        m.email=email
        m.theme=theme
        m.cake=cake
        m.cradle=cradle
        m.entertainment=entertainment
        m.decoration=decoration
        m.balloons=balloons
        m.date=date
        m.guest=guest
        m.location=location
        m.save()
        return redirect('my_bookings')
    return render(request, 'party.html', {'images': images})


def wedding(request):
    images = pictureModel.objects.all() 
    if request.method=='POST':
        form_name=request.POST['form_name']
        username=request.POST['username'] 
        email=request.POST['email'] 
        theme=request.POST['theme'] 
        cake=request.POST['cake'] 
        cradle=request.POST['cradle'] 
        entertainment=request.POST['entertainment'] 
        decoration=request.POST['decoration'] 
        balloons=request.POST['balloons'] 
        date=request.POST['date'] 
        guest=request.POST['guest']
        location=request.POST['location']
        m=HistoryModel()
        m.form_name=form_name
        m.username=username
        m.email=email
        m.theme=theme
        m.cake=cake
        m.cradle=cradle
        m.entertainment=entertainment
        m.decoration=decoration
        m.balloons=balloons
        m.date=date
        m.guest=guest
        m.location=location
        m.save()
        return redirect('my_bookings')
    return render(request, 'wedding.html', {'images': images})


def birthday(request):
    images = pictureModel.objects.all() 
    if request.method=='POST':
        form_name=request.POST['form_name']
        username=request.POST['username'] 
        email=request.POST['email'] 
        theme=request.POST['theme'] 
        cake=request.POST['cake'] 
        cradle=request.POST['cradle'] 
        entertainment=request.POST['entertainment'] 
        decoration=request.POST['decoration'] 
        balloons=request.POST['balloons'] 
        date=request.POST['date'] 
        guest=request.POST['guest']
        location=request.POST['location']
        m=HistoryModel()
        m.form_name=form_name
        m.username=username
        m.email=email
        m.theme=theme
        m.cake=cake
        m.cradle=cradle
        m.entertainment=entertainment
        m.decoration=decoration
        m.balloons=balloons
        m.date=date
        m.guest=guest
        m.location=location
        m.save()
        return redirect('my_bookings')
    return render(request, 'birthday.html', {'images': images})


def anniversary(request):
    images = pictureModel.objects.all() 
    if request.method=='POST':
        form_name=request.POST['form_name']
        username=request.POST['username'] 
        email=request.POST['email'] 
        theme=request.POST['theme'] 
        cake=request.POST['cake'] 
        cradle=request.POST['cradle'] 
        entertainment=request.POST['entertainment'] 
        decoration=request.POST['decoration'] 
        balloons=request.POST['balloons'] 
        date=request.POST['date'] 
        guest=request.POST['guest']
        location=request.POST['location']
        m=HistoryModel()
        m.form_name=form_name
        m.username=username
        m.email=email
        m.theme=theme
        m.cake=cake
        m.cradle=cradle
        m.entertainment=entertainment
        m.decoration=decoration
        m.balloons=balloons
        m.date=date
        m.guest=guest
        m.location=location
        m.save()
        return redirect('my_bookings')
    return render(request, 'anniversary.html', {'images': images})


def getTogether(request):
    images = pictureModel.objects.all() 
    if request.method=='POST':
        form_name=request.POST['form_name']
        username=request.POST['username'] 
        email=request.POST['email'] 
        theme=request.POST['theme'] 
        cake=request.POST['cake'] 
        cradle=request.POST['cradle'] 
        entertainment=request.POST['entertainment'] 
        decoration=request.POST['decoration'] 
        balloons=request.POST['balloons'] 
        date=request.POST['date'] 
        guest=request.POST['guest']
        location=request.POST['location']
        m=HistoryModel()
        m.form_name=form_name
        m.username=username
        m.email=email
        m.theme=theme
        m.cake=cake
        m.cradle=cradle
        m.entertainment=entertainment
        m.decoration=decoration
        m.balloons=balloons
        m.date=date
        m.guest=guest
        m.location=location
        m.save()
        return redirect('my_bookings')
    return render(request, 'getTogether.html', {'images': images})


def privateMeeting(request):
    images = pictureModel.objects.all() 
    if request.method=='POST':
        form_name=request.POST['form_name']
        username=request.POST['username'] 
        email=request.POST['email'] 
        theme=request.POST['theme'] 
        cake=request.POST['cake'] 
        cradle=request.POST['cradle'] 
        entertainment=request.POST['entertainment'] 
        decoration=request.POST['decoration'] 
        balloons=request.POST['balloons'] 
        date=request.POST['date'] 
        guest=request.POST['guest']
        location=request.POST['location']
        m=HistoryModel()
        m.form_name=form_name
        m.username=username
        m.email=email
        m.theme=theme
        m.cake=cake
        m.cradle=cradle
        m.entertainment=entertainment
        m.decoration=decoration
        m.balloons=balloons
        m.date=date
        m.guest=guest
        m.location=location
        m.save()
        return redirect('my_bookings')
    return render(request, 'privateMeeting.html', {'images': images})


def userLogin(request):
    if request.method=="POST":
        name = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = userData1()
        user.username=name
        user.mobile=mobile
        user.email=email
        user.password=make_password(password)        
        user.save()
        return redirect('log_in')
    return render(request,"userLogin.html/",{})       

def log_in(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        password=request.POST.get('password')
        print(make_password(password))
        password=make_password(password)
        user=authenticate(request,email=email,password=password)
        print('user', user)
        if user is not None:
            login(request, user,backend='smart.auth.backend')
            return redirect('events')
        else:
            print('not login...')
    return render(request,"sign_in.html/",{})


def logOut(request):
    logout(request)
    return redirect(reverse('log_in'))

def adminHome(request):

    return render(request,'CeremoAdmin/master_admin.html',{})

def dashboard(request):
    users=userData1.objects.all()
    return render(request,'CeremoAdmin/index.html',{"users": users})

def picture_upload(request):
    if request.method=='POST':
        form=pictureModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'upload was successfull')
            return redirect(reverse('picture_upload'))
    else:
        form=pictureModelForm()
    return render(request,'CeremoAdmin/picUpload.html',{'form':form})

def get_pictures(request):
    images=pictureModel.objects.all()
    return render(request,'CeremoAdmin/get_pictures.html',{'images':images})


def delete_user(request,id):
    u=userData1.objects.get(pk=id)
    u.delete()
    return redirect('/CeremoAdmin/index')

def update_user(request,id):
    u=userData1.objects.get(pk=id)

    return render(request,'CeremoAdmin/update_user.html/',{'u':u})

def updating_user(request):
    if request.method=="POST":
        name = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        user = userData1.objects.get(email=email)
        user.username=name
        user.mobile=mobile
        user.email=email
        user.password=passw
        user.save()
        print('updated')
        return redirect("/dashboard")
    return render(request,'CeremoAdmin/update_user.html/',{})  

def update_profile(request):
    if request.method=="POST":
        name = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = userData1.objects.get(email=email)
        user.username=name
        user.mobile=mobile
        user.email=email
        user.password=make_password(password)        
        user.save()
        messages.success(request,"your information was updated successfully..")
        return redirect(reverse("update_profile"))
    return render(request,'update_profile.html/',{})

def my_bookings(request):
    user=get_session_username(request)
    email=user['email']
    try:
        data = HistoryModel.objects.filter(email=email,status=True)
    except ObjectDoesNotExist:
        messages.error(request,'no Booking is done yet..')
        data = None

    return render(request,'my_bookings.html/',{'data':data,'email':email})

def volunteers(request):
    vols = VolunteerModel.objects.all()

    if request.method == "POST":
        form = volunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Upload was successful')
            return redirect('volunteers')
    else:
        form = volunteerForm()
    return render(request, 'CeremoAdmin/volunteers.html', {'vols': vols, 'form': form})

def all_bookings(request):
    bookings=HistoryModel.objects.all()
    return render(request,'CeremoAdmin/all_bookings.html',{'bookings':bookings})


def admin_login(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        if username == 'Rupesh' and password == 'admin@1234':
            return redirect('adminHome')
        else:
            return render(request, 'CeremoAdmin/admin_login.html', {})
    return render(request, 'CeremoAdmin/admin_login.html')

def cancel_booking(request,id):
    u=HistoryModel.objects.get(pk=id)
    u.status=False
    u.save()
    return redirect('my_bookings')

def delete_booking(request,id):
    u=HistoryModel.objects.get(pk=id)
    u.delete()
    return redirect('/CeremoAdmin/all_bookings')

def assign(request,id):
    if request.method=="POST":
        volunteer = request.POST.get('volunteer')
        contact = request.POST.get('contact')
        u= HistoryModel.objects.get(pk=id)
        u.planner=volunteer+' , '+contact
        u.save()
        return redirect('all_bookings')
    return render(request,'CeremoAdmin/assign_volunteer.html/',{})

def to_gallery(request):
    if request.method=='POST':
        form=GallerModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'upload was successfull')
            return redirect(reverse('to_gallery'))
    else:
        form=pictureModelForm()
    return render(request,'CeremoAdmin/to_gallery.html',{'form':form})

def delete_volunteer(request,id):
    vol=VolunteerModel.objects.get(pk=id)
    vol.delete()
    return redirect('volunteers')

