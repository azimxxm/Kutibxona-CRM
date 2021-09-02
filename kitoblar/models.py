from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


class Lavozim(models.Model):
    Lavozim_nomi = CharField(max_length=100, null=True)
    Kiritilgan_sanasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Xodimlar lavozimi"
        verbose_name_plural = "Xodimlar lavozimi"

    def __str__(self):
        return self.Lavozim_nomi


class Xodimlar(models.Model):
    Rasm = models.ImageField(upload_to="Xodimlar/%Y/%m/", null=True)
    Ism = models.CharField(max_length=100, null=True)
    Yosh = models.IntegerField(default=0, null=True,)
    Telefon = models.BigIntegerField(null=True)
    Lavozimi = models.ForeignKey(Lavozim, on_delete=CASCADE, null=True)
    Manzil = models.CharField(max_length=100, null=True)
    Kiritilgan_sanasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Xodimlar"
        verbose_name_plural = "Xodimlar"

    def __str__(self):
        return self.Ism


class Janir(models.Model):
    Janir_nomi = models.CharField(max_length=100, null=True)
    Kiritilgan_sanasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kitob Janirlari"
        verbose_name_plural = "Kitob Janirlari"

    def __str__(self):
        return self.Janir_nomi


class Nashriyot(models.Model):
    Nashriyot_nomi = models.CharField(max_length=100, null=True)
    Kiritilgan_sanasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kitob Nashriyot nomi"
        verbose_name_plural = "Kitob Nashriyot nomi"

    def __str__(self):
        return self.Nashriyot_nomi


class Kitob_tillari(models.Model):
    Til = models.CharField(max_length=50, null=True)
    Kiritilgan_sanasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kitob tillari"
        verbose_name_plural = "Kitob tillari"

    def __str__(self):
        return self.Til


class Student(models.Model):
    Rasm = models.ImageField(upload_to="Student/%Y/%m/%d/",  blank=True)
    Ism = models.CharField(max_length=100, null=True)
    Yosh = models.IntegerField(default=0, null=True,)
    Telefon = models.BigIntegerField(null=True)
    Manzil = models.CharField(max_length=100, null=True)
    Kiritilgan_sanasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "O'quvchilar"
        verbose_name_plural = "O'quvchilar"

    def __str__(self):
        return self.Ism


class Kitoblar(models.Model):
    Nomi = models.CharField(max_length=100, null=True)
    Isbn = models.BigIntegerField(null=True)
    Nashir_yili = models.DateField(null=True)
    Janir = models.ForeignKey(Janir, on_delete=CASCADE, null=True)
    Nashriyot = models.ForeignKey(Nashriyot, on_delete=CASCADE, null=True)
    Til = models.ForeignKey(Kitob_tillari, on_delete=CASCADE, null=True)
    Rasmi = models.ImageField(upload_to="Kitoblar/%Y/%m/")
    Kiritilgan_sanasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kitoblar"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.Nomi


class Berilgan_kitoblar(models.Model):
    Kitob_nomi = models.ForeignKey(Kitoblar, on_delete=CASCADE, null=True)
    Student = models.ForeignKey(Student, on_delete=CASCADE, null=True, verbose_name="O'quvchi")
    Olingan_sanasi = models.DateTimeField(null=True)
    Qaytarilgan_sanasi = models.DateTimeField(blank=True)
    Kitobning_xolati = models.CharField(max_length=100, blank=True)
    Kiritilgan_sanasi = models.DateTimeField(auto_now_add=True)
    Bergan_xodim = models.ForeignKey(Xodimlar, on_delete=CASCADE, null=True)

    class Meta:
        verbose_name = "Berilgan kitoblar"
        verbose_name_plural = "Berilgan kitoblar"

    def __str__(self):
        return f'{self.Student} - {self.Kitob_nomi}'

