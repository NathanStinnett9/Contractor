from django import forms  # Ensure this import is at the top of the file
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class MyUserCreationForm(UserCreationForm):
    # Add the user_type field to the form
    USER_TYPE_CHOICES = (
        ('company', 'Company'),
        ('job_finder', 'Job Finder'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2', 'user_type']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']