from django.shortcuts import render
from kitoblar.models import *

def view(request):
    kitoblar = Kitoblar.objects.count()
    student = Student.objects.count()
    xodimlar = Xodimlar.objects.count()
    lavozim = Lavozim.objects.count()
    kitob_tillari = Kitob_tillari.objects.count()
    janir = Janir.objects.count()
    student_view = Student.objects.all()
    berilgan_kitoblar = Berilgan_kitoblar.objects.count()
    context = {
        'kitoblar':kitoblar,
        'student':student,
        'xodimlar':xodimlar,
        'lavozim':lavozim,
        'kitob_tillari':kitob_tillari,
        'janir':janir,
        'student_view':student_view,
        'berilgan_kitoblar':berilgan_kitoblar,
    }
    return render(request, 'dashboard/index.html', context)


def forms(request):
    return render(request, 'dashboard/forms.html')


def table(request):
    return render(request, 'dashboard/table.html')


def chart(request):
    return render(request, 'dashboard/chart.html')
