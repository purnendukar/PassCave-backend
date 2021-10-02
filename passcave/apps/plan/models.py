from django.db import models
from utils.base.models import BaseModel

# Create your models here.
class Plan(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    amount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True, 
        blank=True
    )
    no_members = models.IntegerField(
        null=False, 
        blank=False, 
        verbose_name="Number of Members"
    )

