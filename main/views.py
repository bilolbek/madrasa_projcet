from django.shortcuts import render
from main.models import Course
from main.models import Prize
from main.models import Information
from main.models import Filial
from main.models import Staff
from main.models import Vacancy


# Create your views here.


def indexHandler(request):
    courses = Course.objects.filter(status=0)
    prizes = Prize.objects.filter(status=0)
    informations = Information.objects.filter(status=0)
    filials = Filial.objects.filter(status=0)
    vacancies = Vacancy.objects.filter(status=0)
    staffs = Staff.objects.filter(status=0)
    if informations:
        information = informations[0]

    return render(request, 'index.html', {
        'courses': courses,
        'prizes': prizes,
        'information': information,
        'filials': filials,
        'staffs': staffs,
        'vacancies': vacancies,
    })
