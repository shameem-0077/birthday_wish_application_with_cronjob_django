from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MainUser, BirthdayProfile, ProfileRelation, Notification
# Register your models here.
class MainUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_image',)}),
    )

admin.site.register(MainUser, MainUserAdmin)

class BirthdayProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'email', 'name', 'date_of_birth', 'relation','is_deleted',)

admin.site.register(BirthdayProfile, BirthdayProfileAdmin)

class ProfileRelationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

admin.site.register(ProfileRelation, ProfileRelationAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'message', 'birthday_profile')

admin.site.register(Notification, NotificationAdmin)




