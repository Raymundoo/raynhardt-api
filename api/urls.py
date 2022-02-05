from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
	MrOlimpya_APIView, MrOlimpya_APIView_Detail, ListCreateApiViewMrOlimpya,
	home, autor_add_api, autor_delete_api, autor_edit_api)

urlpatterns = [
    # API
    path('v1/mrolimpya/', ListCreateApiViewMrOlimpya.as_view()),
    path('v1/mrolimpya/<int:pk>/', MrOlimpya_APIView_Detail.as_view()),

    # Home
    path('', login_required(home), name='home'),
    path('autor/agregar/', login_required(autor_add_api), name='autor_add_api'),
    path('autor/eliminar/<int:id_autor>/', login_required(autor_delete_api), name='autor_delete_api'),
    path('autor/editar/<int:id_autor>/', login_required(autor_edit_api), name='autor_edit_api'),
]