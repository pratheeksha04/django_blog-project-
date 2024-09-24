from django.contrib.auth.models import User #this to get frontend of users in admin panekl for login/register
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('email','username','password1','password2')