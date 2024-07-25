from django.shortcuts import render
from users.models import *

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        relations = ProfileRelation.active_objects.all()
        birthday_profile_instances = BirthdayProfile.active_objects.filter(user=request.user)
        notifications = Notification.active_objects.filter(birthday_profile__user=request.user)
        context = {
            "title": "Home page",
            "relations":relations,
            "birthday_profile_instances": birthday_profile_instances,
            "notifications": notifications
        }
    else:
        context = {
            "title": "Home page"
        }
    return render(request, 'main/index.html', context=context)
