from django.urls import path

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaUpdate, MascotaDelete

app_name = 'mascotas'
urlpatterns = [
    path('', index, name='index'),
    path('listado/', MascotaList.as_view(), name='mascota_listar'),
    path('nuevo/', mascota_view, name='mascota_crear'),
    path('editar/<pk>/', MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<pk>/', MascotaDelete.as_view(), name='mascota_eliminar'),
]
