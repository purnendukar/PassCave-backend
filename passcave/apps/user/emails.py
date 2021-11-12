import os

# PassCave Stuff
from apps.base.emails import SendTransactionalEmail
from apps.base.utils.urls import resolve_frontend_url
from apps.user.tokens import get_token_for_password_reset


class SendPasswordResetEmail(SendTransactionalEmail):
    EMAIL_ENABLED = True
    SUBJECT = "Reset your Password!"
    TEMPLATE = f"{os.path.dirname(__file__)}/templates/email/forgot_password.html"

    def __init__(self, user):
        self.user = user

    def get_context(self):
        token = get_token_for_password_reset(self.user)
        password_reset_url = resolve_frontend_url("password_confirm", token=token)
        context = {
            "password_reset_url": password_reset_url,
            "user": {
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "email": self.user.email,
            },
        }
        return context

    def get_to_emails(self):
        return [self.user.email]
