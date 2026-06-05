from django.urls import path
from .views import (
    CreatePatient,
    UpdatePatient,
    GetPatientById,
    GetAllPatients,
    DeletePatient
)

urlpatterns = [
    path('create/', CreatePatient.as_view(), name='create_patient'),
    path('update/', UpdatePatient.as_view(), name='update_patient'),
    path('get/', GetPatientById.as_view(), name='get_patient'),
    path('getall/', GetAllPatients.as_view(), name='get_all_patients'),
    path('delete/', DeletePatient.as_view(), name='delete_patient'),
]