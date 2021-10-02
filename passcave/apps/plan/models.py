from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    amount = models.DecimalField(null=True, blank=True)
    no_members = models.IntegerField(null=False, blank=False, verbose_name="Number of Members")

