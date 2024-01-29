from django.db import models
from django.contrib.auth.models import AbstractUser

    
LAVOZIM_ADMIN, LAVOZIM_TYUTR = ('admin', 'tyutr')
YONALISH_MI, YONALISH_FA = ('Matematika-informatika', 'Fizika-asteranomiya')
KURS_1, KURS_2, KURS_3, KURS_4 = ('1', '2', '3', '4')
GURUH_1, GURUH_2, GURUH_3, GURUH_4, GURUH_5, GURUH_6, GURUH_7, GURUH_8 = ('1', '2', '3', '4', '5', '6', '7', '8')  



class User(AbstractUser):  
    LAVOZIM_CHOISE = (
        (LAVOZIM_ADMIN, LAVOZIM_ADMIN),
        (LAVOZIM_TYUTR, LAVOZIM_TYUTR)
    )
    YONLISH_CHOISE = (
        (YONALISH_MI, YONALISH_MI),
        (YONALISH_FA, YONALISH_FA)
    ) 
    KURS_CHOISE = (
        (KURS_1, KURS_1),
        (KURS_2, KURS_2),
        (KURS_3, KURS_3),
        (KURS_4, KURS_4)
    )
    lavozim = models.CharField(max_length=10, choices=LAVOZIM_CHOISE, default=LAVOZIM_TYUTR)
    yonalish = models.CharField(max_length=50, choices=YONLISH_CHOISE, default=YONALISH_MI)
    kurs = models.CharField(max_length=2, choices=KURS_CHOISE, default=KURS_1)


    def __str__(self):
        return self.username
    



