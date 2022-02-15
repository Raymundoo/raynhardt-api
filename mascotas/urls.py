from django.urls import path
from mascotas.views import ListCreateApiViewMascota, MascotaAPIViewDetail, mascota_lista_api

urlpatterns = [
    # Endpoints
    path('v1/mascota/', ListCreateApiViewMascota.as_view(), name='list_create_apiview_mascota'),
    path('v1/mascota/<int:pk>/', MascotaAPIViewDetail.as_view(), name='mascota_apiview_detail'),

    # Mascotas APÏ
    path('mascota/lista/', mascota_lista_api, name="mascota_lista_api"),
]
