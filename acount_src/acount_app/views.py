""" registration and login views """
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

#---------------------------------user registration-----------------------------#

def registration(request):
    """user register"""
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            # we grap all the user_data and save it to the database

            user = user_form.save()  

            # hashing of the password by calling the set_pass function

            user.set_password(user.password)
            user.save() # saving password

            profile = profile_form.save(commit=False)
            profile.user = user  # here is the one-to-one linkage "model and form"

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'acount_app/register.html', {"user_form":user_form, "profile_form":profile_form, 'registered':registered})
          
#---------------------------------loging user-----------------------------#
# def user_login(request):
#     "loging in users"
#     if request.method == 'POST':
#         user_form = LoginForm(data=request.POST)
#         if user_form.is_valid():
#             username_password = user_form.cleaned_data
#             user = authenticate(
#                 username=username_password['username'], password=username_password['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse('Disable account')
#         else:
#             up = user_form.cleaned_data
#             print(f"username => {up['username']} password => {up['password']}")
#             return HttpResponse('invalid username or password')
#     else:
#         user_form = LoginForm()
#     return render(request, 'acount_app/login.html', {'user_form':user_form})
        


def user_login(request):
    user_form = LoginForm(request.POST or None)
    if request.method == 'POST' and user_form.is_valid():
        user = user_form.authenticate_user()
        login(request, user)
        return HttpResponseRedirect(reverse("acount_app:dashboard"))

    return render(request, 'registration/login.html', {'user_form': user_form})


#---------------------------------index page-----------------------------#
def index(request):
    """index page"""
    return render(request, 'acount_app/index.html', {'home':'home'})

#---------------------------------logout-----------------------------#
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#---------------------------------User Dashboad-----------------------------#


@login_required
def user_dashboard(request):
    """Dashboad"""
    return render(request, "acount_app/user_dash.html",{'section':'dashboard'})

#---------------------------------special func-----------------------------#


@login_required
def special_msg(request):
    return HttpResponse(f'lllll {request.get(username)}')
