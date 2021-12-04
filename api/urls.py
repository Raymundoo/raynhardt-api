from django.urls import path
from .views import MrOlimpya_APIView, MrOlimpya_APIView_Detail

app_name = 'api'

urlpatterns = [
    path('v1/mrolimpya', MrOlimpya_APIView.as_view()), 
    path('v1/mrolimpya/<int:pk>/', MrOlimpya_APIView_Detail.as_view()),   
]