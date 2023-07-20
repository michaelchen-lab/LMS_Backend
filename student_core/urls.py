from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student_core.views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'initial', StudentInitialViewSet, basename="student_initial")
router.register(r'submission', StudentSubmissionViewSet, basename="student_submission")
router.register(r'submission_status', StudentSubmissionStatusViewSet, basename="student_submission_status")
router.register(r'resource', StudentResourceViewSet, basename="student_resource")
router.register(r'enroll', EnrollViewSet, basename="student_enroll")
router.register(r'portfolio', StudentPortfolioViewSet, basename="student_portfolio")
router.register(r'group_submission', GroupSubmissionViewSet, basename="student_group_submission")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('leaderboard', Leaderboard, name="leaderboard"),
    path('', include(router.urls))
]
