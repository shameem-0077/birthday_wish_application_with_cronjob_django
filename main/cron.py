from datetime import date
from mailqueue.models import MailerMessage

from users.models import BirthdayProfile, Notification

def send_birthday_wish_job():
    today = date.today()
    birthday_profiles = BirthdayProfile.active_objects.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)

    if birthday_profiles.exists():
        for birthday_profile in birthday_profiles:
            if not Notification.active_objects.filter(birthday_profile=birthday_profile, date_added__date=today, is_sended=True).exists():
                new_message = MailerMessage()
                new_message.subject = birthday_profile.email_subject
                new_message.to_address = birthday_profile.email
                new_message.from_address = birthday_profile.user.email
                new_message.html_content = birthday_profile.email_content
                new_message.app = "main"
                new_message.save()
                try:
                    new_message.send_mail()
                
                    Notification.objects.create(
                        title="Success",
                        message="Email Sended",
                        birthday_profile=birthday_profile,
                        is_sended=True
                    )
                except:
                    Notification.objects.create(
                        title="Failed",
                        message="Email Failed",
                        birthday_profile=birthday_profile
                    )

            

  