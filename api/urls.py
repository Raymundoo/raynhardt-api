from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MrOlimpya_APIView, MrOlimpya_APIView_Detail, ListCreateApiViewMrOlimpya, home

urlpatterns = [
    # API
    path('v1/mrolimpya/', ListCreateApiViewMrOlimpya.as_view()),
    path('v1/mrolimpya/<int:pk>/', MrOlimpya_APIView_Detail.as_view()),

    # Home
    path('', login_required(home)),
]