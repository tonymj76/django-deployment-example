from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate

#---------------------------------loginform advance-----------------------------#
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
    )

    def clean(self):
        user = self.authenticate_via_email()
        if not user:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
        else:
            self.user = user
        return self.cleaned_data

    def authenticate_user(self):
        return authenticate(
            username=self.user.username,
            password=self.cleaned_data['password'])

    def authenticate_via_email(self):
        """
            Authenticate user using email.
            Returns user object if authenticated else None
        """
        email = self.cleaned_data['email']
        if email:
            try:
                user = User.objects.get(email__iexact=email)
                if user.check_password(self.cleaned_data['password']):
                    return user
            except ObjectDoesNotExist:
                pass
        return None
#---------------------------------html login form-----------------------------#


# class LoginForm(forms.Form):
#     """user login form"""
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

#---------------------------------creating forms details-----------------------------#

#---------------------------------registration form-----------------------------#

class UserForm(forms.ModelForm):
    """creating the user form that links from User"""
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('postfolio', 'profile_pic')




  
