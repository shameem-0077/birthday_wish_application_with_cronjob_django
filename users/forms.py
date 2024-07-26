from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import MainUser


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        required=True
    )


class CreateAccountForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "First name*"})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Last name*"})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email*"})
    )
    profile_image = forms.ImageField(
        required=False,  # Set to True if the image is required
        widget=forms.FileInput(attrs={"placeholder": "Upload a Profile Picture"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password*"}),
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password*"}),
        required=True
    )

    class Meta:
        model = MainUser
        fields = ["username", "first_name", "last_name", "email", "profile_image"]
    

    def clean(self):
        cleaned_data = super().clean()
        profile_image = cleaned_data.get('profile_image', None)
        if not profile_image:
            raise forms.ValidationError("Please upload a profile image")
        
        return cleaned_data

    def save(self, commit=True):
        user = super(CreateAccountForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



        


