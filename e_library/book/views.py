from django.conf import settings
from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .models import Book
from .forms import BookForm
from django.urls import reverse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User


"""from .forms import BookForm ,UserRegistrationForm, UserLoginFrom
from django.contrib.auth import(
        authenticate,
        login,
        logout,
        get_user_model
    )
"""
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('book:login'))
    context={
        'viewTitle':"About E-Library Management System"
    }
    template="home.html"
    return render(request, template, context)

def book_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('book:login'))
    qs=Book.objects.all()
    context={
        'book_list':qs
    }
    template="book_list.html"
    return render(request,template,context)


def book_detail(request, id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('book:login'))
    qs = Book.objects.get(id=id)
    context = {
        'book': qs
    }
    template = "book_detail.html"
    return render(request, template, context)


def book_create(request,id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('book:login'))
    form=BookForm(request.POST or None)
    context={
        'form':form
    }
    if form.is_valid():
        obj=form.save(commit=False)
        obj=form.save()
        context = {
            'form': BookForm
        }
    template = "book_create.html"
    return render(request, template, context)


def book_update(request,id=None):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('book:login'))
    obj=Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=obj)
    context={
        'obj':obj,
        'form':form
    }
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        return HttpResponseRedirect('/book/{num}/detail'.format(num=obj.id))
    template="book_update.html"
    return render(request, template, context)

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('book:login'))
    else:
        return render(request, 'book/dashboard.html')

def mylogin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('book:dashboard'))
        else:
            return HttpResponseRedirect(reverse('book:login'))
    else:
        return render(request,'book/login.html')
def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('book:login'))

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
##        email_list=['navinpnchal@gmail.com',email]
        print(email)
##        send_mail(
##            'library membership',
##            'Congratulation u r registered.',
##            settings.EMAIL_HOST_USER,
##            [email_list],
##            fail_silently=False,
##        )
        user = User.objects.create_user(username,email, password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('book:map'))
        else:
            return HttpResponseRedirect(reverse('book:login'))
    else:
        return render(request, 'book/register.html')
def map(request):
    return render(request,'map.html',{})





