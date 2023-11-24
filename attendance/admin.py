from django.contrib import admin

from attendance.models import Course, Semester, Class, Enrollment, CollegeDay, Lecturer, Student, Attendance

# Register your models here.

admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Class)
admin.site.register(Enrollment)
admin.site.register(CollegeDay)
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Attendance)
