from django.db import models


YONALISH_MI, YONALISH_FA = ('Matematika-informatika', 'Fizika-asteranomiya')
KURS_1, KURS_2, KURS_3, KURS_4 = ('1', '2', '3', '4')
GURUH_1, GURUH_2, GURUH_3, GURUH_4, GURUH_5, GURUH_6, GURUH_7, GURUH_8 = ('1', '2', '3', '4', '5', '6', '7', '8')  

class Yonalish(models.Model):
    YONLISH_CHOISE = (
        (YONALISH_MI, YONALISH_MI),
        (YONALISH_FA, YONALISH_FA)
    ) 
    name = models.CharField(max_length=50, choices=YONLISH_CHOISE, default=YONALISH_MI)

    def __str__(self):
        return self.name 
    
class Kurs(models.Model):
    KURS_CHOISE = (
        (KURS_1, KURS_1),
        (KURS_2, KURS_2),
        (KURS_3, KURS_3),
        (KURS_4, KURS_4)
    )
    name = models.CharField(max_length=50, choices=KURS_CHOISE, default=KURS_1)

    def __str__(self):
        return self.name
    
class Guruh(models.Model):
    GURUH_CHOISE = (
        (GURUH_1, GURUH_1),
        (GURUH_2, GURUH_2),
        (GURUH_3, GURUH_3),
        (GURUH_4, GURUH_4),
        (GURUH_5, GURUH_5),
        (GURUH_6, GURUH_6),
        (GURUH_7, GURUH_7),
        (GURUH_8, GURUH_8)
    )
    name = models.CharField(max_length=50, choices=GURUH_CHOISE, default=GURUH_1)

    def __str__(self):
        return self.name


    
class Team(models.Model):
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
     

    def __str__(self):
        data = f'{self.yonalish}-yonalish {self.kurs}-kurs {self.guruh}-guruh'
        return data
    


class Worker(models.Model):
    fish = models.CharField(max_length=250)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="workers")


    def __str__(self):
        return self.fish

class Attendance(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.team.yonalish)} jamoasining {str(self.date)} sanadagi davomadi."
    


class Mark(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='marks')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="marks")
    is_attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ['attendance', 'worker']