from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('vistapeliculas/',views.vistapeliculas),
    path('registrarCurso/', views.registrarCurso),
    path('eliminacionCurso/<codigo>', views.eliminacionCurso),
    path('comentarioCurso/<codigo>',views.comentarioCurso),
    path('editarCurso/' , views.editarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),


]

