# Generated by Django 4.2.14 on 2024-07-24 19:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilerelation_birthdayprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthdayprofile',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]
