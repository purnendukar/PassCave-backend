from django.db import models

from apps.base.models import BaseModel
from apps.user.models import User

# Create your models here.
class Organisation(BaseModel):
    ORG_TYPE_CHOICES = [("family", "Family"), ("organisation", "Organisation")]
    org_type = models.TextField(
        choices=ORG_TYPE_CHOICES, null=True, blank=True, default=2
    )
    admin = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="owned_organisation",
        null=True,
        blank=True,
    )
    members = models.ManyToManyField(to=User, related_name="organisations")
