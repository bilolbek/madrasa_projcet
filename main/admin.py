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
# Register your models here.

