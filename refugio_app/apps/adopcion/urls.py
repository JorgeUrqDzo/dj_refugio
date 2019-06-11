from django.urls import path

from apps.adopcion.views import SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

app_name = 'adopcion'
urlpatterns = [
    path('solicitud/listar/', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva/', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solicitud/editar/<pk>', SolicitudUpdate.as_view(),
         name='solicitud_editar'),
    path('solicitud/eliminar/<pk>', SolicitudDelete.as_view(),
         name='solicitud_eliminar'),

]
