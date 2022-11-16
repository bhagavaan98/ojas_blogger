from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from . forms import SignUpForm,ContactForm,blogForm
from . models import blog
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.core.cache import cache
from django.core.mail import send_mail

# Create your views here.
#base function
def base_details(request):
    return render(request,'base.html')

#contact form
def contact_details(request):
    if request.method=="POST":
        fm=ContactForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Thanks For Sharing Your contacts")
            print("thanks for using")
    else:
        fm=ContactForm()
    return render(request,'contact.html',{'form':fm})

#blog form
def blog_details(request):
    if request.method=="POST":
        fm=blogForm(request.POST)
        if fm.is_valid():
            print("Form is validated")
            ti=fm.cleaned_data['title']
            con=fm.cleaned_data['content']
            ob=blog(title=ti,content=con)
            ob.save()
            # fm=blogForm()
            # messages.success(request,"Your message sent successfully")
            # ob1=blog.objects.all()
            # return HttpResponseRedirect('/home',{"form":fm,"ob1":ob1})
    else:
        fm=blogForm()
    ob1=blog.objects.all()
    ip=request.session.get('ip')
    return render(request,'blog.html',{'form':fm,'ob1':ob1,'ip':ip})



def home_details(request):
    fm=blog.objects.all()
    user = request.us
    ct = cache.get('count', version=user.pk)
    return render(request,'home.html',{'form':fm,'ct':ct})

def update_details(request,id):
    ab=blog.objects.get(pk=id)
    fm=blogForm(request.POST,instance=ab)
    if request.method=="POST":
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        return render(request,'update.html',{'form':fm})

def delete(request,id):
    pi=blog.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')


#signup view function
def sign_up(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Your Account Created Successfully!!")
            fm.save()
    else:
        fm=SignUpForm()
    return render(request,'signup.html',{'form':fm})

#login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in successfully!!")
                return HttpResponseRedirect("/blog/")
        else:
            fm=AuthenticationForm()
        return render(request,'userlogin.html',{"form":fm})
    else:
        return HttpResponseRedirect("/blog/")

#profile
def profile_details(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login')



#logout
def user_logout(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return HttpResponseRedirect('/login/')


def show(reqeust):
    send_mail(
        'Requesting to join early',
        'Hi, Please join us in the meeting early',
        'chbhagavaan98@gmail.com',
        ['chsravani1004@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("<h1>Mail Sent</h1>")
