from django.db import models

# Create your models here.
class BabyYet(models.Model):
    baby_yet = models.BooleanField(default=False)
    diapers_url = models.URLField(default=None, null=True, blank=True)
