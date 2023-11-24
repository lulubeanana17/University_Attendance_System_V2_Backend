from django.contrib.auth.models import User
from rest_framework import serializers

from attendance.models import Semester, Course, Lecturer, Student, Enrollment, Class, CollegeDay, Attendance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name"]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ["id", "dob", "lecturerInfo"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "dob", "studentInfo"]

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ["id", "semester", "year"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "semester", "code", "name"]

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ["id", "student"]

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["id", "number", "course", "enrollments", "lecturer"]

class CollegeDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeDay
        fields = ["id", "classInfo", "students"]

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'class_info', 'enrollment', 'status', 'date']
