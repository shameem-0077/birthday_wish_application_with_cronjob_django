from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login as auth_login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseRedirect

from users.functions import *
from users.models import *
from users.forms import LoginForm, CreateAccountForm

# Create your views here.

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request=request, user=user)
                return redirect(reverse("main_urls:home_url"))
            else:
                messages.error(request, "Invalid credentials")
                return redirect(reverse("users_urls:signin_url"))
        else:
            error_message = generate_form_errors(form)
            messages.error(request, str(error_message))
            return redirect(reverse("users_urls:signin_url"))
    context = {
        "form": form
    }
    return render(request, 'users/login.html', context=context)


def signup(request):
    form = CreateAccountForm()

    if request.method == 'POST':
        form = CreateAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # username = request.POST.get('username', None)
            # first_name = request.POST.get('first_name', None)
            # last_name = request.POST.get('last_name', None)
            # email = request.POST.get('email', None)
            # photo = request.FILES.get('photo', None)
            # password = request.POST.get('password', None)

            # user = MainUser.objects.create_user(
            #     username=username,
            #     email=email,
            #     first_name=first_name,
            #     last_name=last_name,
            #     profile_image=photo,
            #     password=password,
            # )
            
            return redirect(reverse('users_urls:signin_url'))
        else:
            error_message = generate_form_errors(form)
            messages.error(request, str(error_message))
    context = {
        "form": form
    }
    return render(request, 'users/signup.html', context=context)


def logout_user(request):
    logout(request)
    form = LoginForm()

    context = {
        'title': 'Login',
        "form": form
    }
    return render(request, 'users/login.html', context=context)


@require_http_methods(["POST"])
def create_birthday_profile(request):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    photo = request.FILES.get('photo', None)
    dob = request.POST.get('dob', None)
    relation = request.POST.get('relation', None)
    email_subject = request.POST.get('email_subject', None)
    email_content = request.POST.get('email_content', None)


    if not BirthdayProfile.active_objects.filter(email=email, user=request.user).exists():
        relation = ProfileRelation.active_objects.get(pk=relation)
        profile = BirthdayProfile.active_objects.create(
            name=name,
            user=request.user,
            email=email,
            profile_image=photo,
            date_of_birth=dob,
            relation=relation,
            email_subject=email_subject,
            email_content=email_content
        )

        messages.success(request, "Birthday Profile Created Successfully")
    else:
        messages.error(request, "Birthday Profile Already Exists")
    
    return redirect(reverse('main_urls:home_url'))


@require_http_methods(["POST"])
def delete_profile(request, pk):
    if BirthdayProfile.active_objects.filter(pk=pk, user=request.user).exists():
        profile_instance = BirthdayProfile.active_objects.get(pk=pk)
        profile_instance.is_deleted = True
        profile_instance.save()

        messages.success(request, "Birthday Profile Deleted Successfully")
    else:
        messages.error(request, "Birthday Profile Not Found")
    
    return redirect(reverse('main_urls:home_url'))


@require_http_methods(["POST"])
def edit_birthday_profile(request, pk):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    photo = request.FILES.get('photo', None)
    dob = request.POST.get('dob', None)
    relation = request.POST.get('relation', None)
    email_subject = request.POST.get('email_subject', None)
    email_content = request.POST.get('email_content', None)

    if BirthdayProfile.active_objects.filter(pk=pk, user=request.user).exists():
        relation = ProfileRelation.active_objects.get(pk=relation)
        profile_instance = BirthdayProfile.active_objects.get(pk=pk, user=request.user)
        BirthdayProfile.active_objects.update(
            name=name,
            user=request.user,
            email=email,
            date_of_birth=dob,
            relation=relation,
            email_subject=email_subject,
            email_content=email_content,
        )
        if photo:
            profile_instance.profile_image = photo
            profile_instance.save()

        messages.success(request, "Birthday Profile Edited")
    else:
        messages.error(request, "Birthday Profile Not Found")
    return redirect(reverse('main_urls:home_url'))
    

    


