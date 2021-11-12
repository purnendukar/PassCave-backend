from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class SendTransactionalEmail:
    TEMPLATE = None
    SUBJECT = ""
    EMAIL_ENABLED = False

    def get_to_emails(self):
        raise NotImplementedError("This method needs to be implemented")

    def get_cc_emails(self):
        return None

    def get_bcc_emails(self):
        return None

    def get_group_id(self):
        return None

    def get_body(self):
        return None

    def get_attachments(self):
        return None

    def get_context(self):
        raise NotImplementedError("Email Context not provided")

    def get_email_subject(self):
        if not self.SUBJECT:
            raise NotImplementedError("Email Subject not provided")
        return self.SUBJECT

    def get_template(self):
        if not self.TEMPLATE:
            raise NotImplementedError("Email Template not provided")
        return self.TEMPLATE

    def is_email_enabled(self):
        return self.EMAIL_ENABLED

    def get_from_email(self):
        return settings.DEFAULT_FROM_EMAIL

    def send_email(self):
        context = self.get_context()
        template = render_to_string(self.get_template(), context)
        if self.is_email_enabled():
            message = EmailMultiAlternatives(
                subject=self.get_email_subject(),
                body=self.get_body(),
                from_email=self.get_from_email(),
                cc=self.get_cc_emails(),
                to=self.get_to_emails(),
                bcc=self.get_bcc_emails(),
                attachments=self.get_attachments(),
            )
            message.attach_alternative(template, "text/html")
            message.send(fail_silently=False)
