from django.db import models
from users.models import Talaba, Fakultet, Talaba

class Davomat(models.Model):
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE, related_name='davomat')
    kun = models.DateField(auto_now_add=True)

    def __str__(self):
        data = f'{self.fakultet}'
        return data
    

class Baza(models.Model):
    davomat = models.ForeignKey(Davomat, on_delete=models.CASCADE, related_name='baza')
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE, related_name='baza')
    is_attended = models.BooleanField(default=False)
    amaliyot = models.BooleanField(default=False)

    class Meta:
        unique_together = ['davomat', 'talaba']

    def __str__(self):
        data = f'{self.davomat} {self.talaba}'
        return data