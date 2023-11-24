
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from attendance.views import index, semester_list, upload_students_from_excel, UserTypeCheckView, get_enrollment_id
from attendance.viewsets import SemesterViewSet, CourseViewSet, UserViewSet, LecturerViewSet, StudentViewSet, \
    EnrollmentViewSet, ClassViewSet, AttendanceViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("lecturers", LecturerViewSet, basename="lecturers")
router.register("students", StudentViewSet, basename="students")
router.register("semesters", SemesterViewSet, basename="semesters")
router.register("courses", CourseViewSet, basename="courses")
router.register("enrollments", EnrollmentViewSet, basename="enrollments")
router.register("classes", ClassViewSet, basename="classes")
router.register("attendances", AttendanceViewSet, basename="attendances")

urlpatterns = [
    path('', index, name="Home"),
    path("semester_lists/", semester_list, name="semester_list"),
    path("api/", include(router.urls)),
    path("upload_students/", upload_students_from_excel, name="upload_students"),
    path("verify_user/", UserTypeCheckView.as_view(), name="verifyUsers"),
    path("get_enrollment_id/", get_enrollment_id, name="get_enrollment_id"),
]
