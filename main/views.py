from django.shortcuts import render
from main.models import Course
from main.models import Prize
from main.models import Information
from main.models import Filial
from main.models import Staff
from main.models import Vacancy
from main.models import Register
from django.http.response import JsonResponse


# Create your views here.


def indexHandler(request):
    if request.method == 'GET':
        courses = Course.objects.filter(status=0).order_by('rating')
        prizes = Prize.objects.filter(status=0).order_by('rating')
        informations = Information.objects.filter(status=0)
        filials = Filial.objects.filter(status=0).order_by('rating')
        vacancies = Vacancy.objects.filter(status=0)
        staffs = Staff.objects.filter(status=0).order_by('rating')
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

    else:
        r = Register()
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        r.name = name
        r.phone = phone
        r.filial_id = int(address)
        r.save()
        print(JsonResponse({'success': True, 'errorMsg': '', '_success': True}))
        return JsonResponse({'success': True, 'errorMsg': '', '_success': True})
