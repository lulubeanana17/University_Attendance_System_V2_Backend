from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from attendance.models import Semester, Course, Lecturer, Student, Enrollment, Class, Attendance
from attendance.permissions import IsAdmin
from attendance.serializer import SemesterSerializer, CourseSerializer, UserSerializer, LecturerSerializer, \
    StudentSerializer, EnrollmentSerializer, ClassSerializer, AttendanceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsAdmin],
        'update': [IsAdmin],
        'partial_update': [IsAdmin],
        'destroy': [IsAdmin]
    }

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
