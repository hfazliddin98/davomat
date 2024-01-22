from django.db import models
from users.models import Talaba

class Davomat(models.Model):
    talaba_id = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kun = models.DateField(auto_now=True)
    bor = models.BooleanField(default=False)
    yoq = models.BooleanField(default=False)
    amaliyot = models.BooleanField(default=False)
    olinmadi = models.BooleanField(default=False)