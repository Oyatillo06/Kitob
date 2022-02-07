from django.db import models

class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    erkak = models.BooleanField()

    def __str__(self):
        return f"{self.ism}, {self.yosh}"
class Student(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    erkak = models.BooleanField()
    guruh = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.ism}, {self.guruh}"
class Fan(models.Model):
    nom=models.CharField(max_length=30)
    yonalish=models.CharField(max_length=30)
    asosiy=models.BooleanField()
    ustoz=models.ForeignKey(Ustoz, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom},{self.yonalish}"
class Kitob(models.Model):
    T=(
        ("badiy","badiy"),
        ("ilmiy","ilmiy"),
    )
    nom=models.CharField(max_length=20)
    sahifa=models.SmallIntegerField()
    tur=models.CharField(max_length=10,choices=T)
    def __str__(self):
        return f"{self.nom},{self.sahifa},{self.tur}"

class Muallif(models.Model):
    T=(
        ("erkak","erkak"),
        ("ayol","ayol"),


       )
    ism=models.CharField(max_length=30)
    yosh=models.SmallIntegerField()
    jinsi=models.CharField(max_length=5,choices=T)
    def __str__(self):
        return f"{self.ism},{self.yosh}"

class Record(models.Model):
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE)
    olingan_sana=models.DateField()
    def __str__(self):
        return f"{self.muallif},{self.kitob},{self.olingan_sana}"






