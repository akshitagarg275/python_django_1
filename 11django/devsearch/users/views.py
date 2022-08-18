from django.shortcuts import render
from .models import Profile
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"USername does not exist")
        
        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,"Username or password is incorrect")

    return render (request , 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def profiles(request):
    profiles= Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html',context)


def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkill = profile.skill_set.exclude(description__exact = "")
    otherSkill = profile.skill_set.filter(description__exact = "")
    context = {'profile':profile,'topSkill':topSkill , 'otherSkill':otherSkill}

    return render(request, 'users/user-profile.html',context)