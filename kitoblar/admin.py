from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(Lavozim)
class LavozimAdmin(admin.ModelAdmin):
    list_display = ['id', 'Lavozim_nomi', 'Kiritilgan_sanasi']


@admin.register(Xodimlar)
class XodimlarAdmin(admin.ModelAdmin):
    list_display = ['id', 'Ism', 'Yosh', 'Telefon',
                    'Lavozimi', 'Manzil', 'Kiritilgan_sanasi', 'photo_view']
    list_filter = ['Lavozimi', ]
    search_fields = ['Ism', 'Yosh', 'Telefon', 'Manzil']

    def photo_view(self, object):
        if object.Rasm:
            return mark_safe(f"<img src='{object.Rasm.url}' width=40>")

    photo_view.short_description = "Rasm"


@admin.register(Janir)
class JanirAdmin(admin.ModelAdmin):
    list_display = ['id', 'Janir_nomi', 'Kiritilgan_sanasi']


@admin.register(Nashriyot)
class NashriyotAdmin(admin.ModelAdmin):
    list_display = ['id', 'Nashriyot_nomi', 'Kiritilgan_sanasi']


@admin.register(Kitob_tillari)
class Kitob_tillariAdmin(admin.ModelAdmin):
    list_display = ['id', 'Til', 'Kiritilgan_sanasi']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'Ism', 'Yosh', 'Telefon',
                    'Manzil', 'Kiritilgan_sanasi', 'photo_view']
    search_fields = ['Ism', 'Yosh', 'Telefon', 'Manzil']

    def photo_view(self, object):
        if object.Rasm:
            return mark_safe(f"<img src='{object.Rasm.url}' width=40>")

    photo_view.short_description = "Rasm"

@admin.register(Kitoblar)
class KitoblarAdmin(admin.ModelAdmin):
    list_display = ['id', 'Nomi', 'Isbn', 'Nashir_yili',
                    'Janir', 'Nashriyot', 'Til', 'Kiritilgan_sanasi', 'photo_view']
    search_fields = ['Nomi', 'Isbn', 'Nashir_yili',
                     'Qaytarilgan_sanasi', 'Janir', 'Nashriyot', 'Til', ]
    
    def photo_view(self, object):
        if object.Rasmi:
            return mark_safe(f"<img src='{object.Rasmi.url}' width=40>")

    photo_view.short_description = "Rasm"

@admin.register(Berilgan_kitoblar)
class Berilgan_kitoblarAdmin(admin.ModelAdmin):
    list_display = ['id', 'Kitob_nomi', 'Student', 'Olingan_sanasi',
                    'Qaytarilgan_sanasi', 'Bergan_xodim', 'Kitobning_xolati', 'Kiritilgan_sanasi']
    search_fields = ['Kitob_nomi', 'Student',
                     'Olingan_sanasi', 'Qaytarilgan_sanasi']
