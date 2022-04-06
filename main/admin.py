from django.contrib import admin

from main.models import *


class FilialAdmin(admin.ModelAdmin):
    pass


admin.site.register(Filial, FilialAdmin)


class RegisterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Register, RegisterAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)


class PrizeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Prize, PrizeAdmin)


class InformationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Information, InformationAdmin)


class StaffAdmin(admin.ModelAdmin):
    pass


admin.site.register(Staff, StaffAdmin)


class VacancyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
# Register your models here.
