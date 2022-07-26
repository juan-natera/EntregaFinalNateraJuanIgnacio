from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView





urlpatterns = [
    path("", views.inicio, name="Inicio"), #esta era nuestra primer view
    path("cursos", views.cursos, name="Cursos"),
    path("profesores", views.profesores, name="Profesores"),
    path("estudiantes", views.estudiantes, name="Estudiantes"),
    path("entregables", views.entregables, name="Entregables"),
    path('cursoFormulario', views.cursos, name="CursoFormulario"),
    path('profesorFormulario', views.profesores, name="ProfesorFormulario"),
    path('estudianteFormulario', views.estudiantes, name="EstudiantesFormulario"),
    path('entregableFormulario', views.entregables, name="EntregablesFormulario"),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path('curso/detail', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    ]

#path(r'^$', views.CursoList.as_view(), name='list'),
    #path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='detail'),
    #path(r'^nuevo$', views.CursoCreacion.as_view(), name='new'),
    #path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='edit'),
    #path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='delete'),


# ACLARACIÓN IMPORTANTE!!!!!!!
# path(r'^(?P<pk>\d+)$'
# Es una expresión regular, que se compara con la URL real.
# Aquí r'' especifica que la cadena es una cadena sin procesar.
# '^' significa el comienzo y $ marca el final.
# Ahora 'pk' (cuando está dentro de <>) representa una clave principal.
# Una clave principal puede ser cualquier cosa, por ejemplo.
# puede ser una cadena, un número, etc.
# Una clave principal se usa para diferenciar diferentes columnas
# de una tabla. aqui esta escrito.
#<pk>\d+ \d coincide con [0-9] y otros caracteres de dígitos.
#'+' significa que debe haber al menos 1 o más dígitos en el número.