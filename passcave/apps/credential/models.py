from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from utils.base.models import BaseModel
from apps.user.models import User

# Create your models here.
class BankCard(BaseModel):
    card_number = models.CharField(
        max_length= 4*4
    )
    

class Credential(BaseModel):
    limit = models.Q(app_label='credential', model='brand') | \
            models.Q(app_label='credential', model='creator') | \
            models.Q(app_label='credential', model='agency')
    cred_type = models.ForeignKey(
        ContentType, 
        limit_choices_to=limit,
        on_delete=models.CASCADE
    )
    owned_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    owned_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="credential_owned",
        null=False,
        blank=False
    )
    access_given = models.ManyToManyField(
        to=User,
        related_name="credential_access"
    )
    object_id = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    detail = GenericForeignKey(
        'cred_type',
        'object_id'
    )
