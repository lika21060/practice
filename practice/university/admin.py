from django.contrib import admin

# Register your models here.
from university.models import Student,Profile,Course,Professor,Class

admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Class)