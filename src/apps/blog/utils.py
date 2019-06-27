from django.core.mail import send_mail


def new_post_email(users, post_link):
    emails = [user.email for user in users]
    for email in emails:
        send_mail(
            'you have a new post in your news feed',
            f'{post_link}',
            'not-reply@example.com',
            [email],
            fail_silently=False,
        )
