# Generated by Django 4.2.14 on 2024-07-25 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_birthdayprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthdayprofile',
            name='email_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='birthdayprofile',
            name='email_subject',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
