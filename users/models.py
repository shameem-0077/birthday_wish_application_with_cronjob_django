import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

NOTIFICATION_STATUS = (
    ('on_queue', 'On queue'),
    ('delivered', 'Delivered'),
    ('failed', 'Failed'),
)

class MainUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().exclude(is_deleted=True)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return super(DeletedManager, self).get_queryset().filter(is_deleted=True)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    # Model managers
    objects = models.Manager()
    active_objects = ActiveManager() 
    deleted_objects = DeletedManager() 

    class Meta:
        abstract = True

class ProfileRelation(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)


class BirthdayProfile(BaseModel):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    profile_image = models.ImageField(upload_to='birthday/profile_images/', null=True, blank=True)
    date_of_birth = models.DateField()
    relation = models.ForeignKey(ProfileRelation, on_delete=models.CASCADE)
    email_subject = models.CharField(max_length=128, null=True, blank=True)
    email_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Notification(BaseModel):
    title = models.CharField(max_length=128)
    message = models.TextField(null=True, blank=True)
    birthday_profile = models.ForeignKey(BirthdayProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)




