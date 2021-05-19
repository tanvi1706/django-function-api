from django.urls import path
from jboffers.api.views import JobBoardListView, JobBoardDetailView

urlpatterns = [
      path("jobs/", JobBoardListView, name="job-list"),
      path("jobs/<int:pk>/", JobBoardDetailView, name="job-details")

]