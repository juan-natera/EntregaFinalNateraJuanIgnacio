from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregable, Avatar
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def curso(self): # Primera carga de datos a mi base de datos, cargue un curso y una camada (se lo conoce como hacer un insert)
    
    curso = Curso(nombre = "DJ", camada = "11223349")
    
    curso.save

    documento = f"El curso es : {curso.nombre}, la camada : {curso.camada}"

    return HttpResponse(documento)

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):

    return render(request, "AppCoder/estudiantes.html")

def entregables(request):

    return render(request, "AppCoder/entregables.html")

@login_required
def cursos(request):
    
      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})

def profesores(request):
    
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

def estudiantes(request):
    
      if request.method == 'POST':

            miFormulario = EstudianteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email']) 

                  estudiante.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= EstudianteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})

def entregables(request):
    
      if request.method == 'POST':

            miFormulario = EntregableFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  entregable = Entregable (nombre=informacion['nombre'], fechaDeEntrega=informacion['fechaDeEntrega'],
                   entregado=informacion['entregado']) 

                  entregable.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= EntregableFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/entregables.html", {"miFormulario":miFormulario})

def buscar(request):
    
      if  request.GET["camada"]: #if request.method == 'Get':

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
            camada = request.GET["camada"]
            print(camada)
            
            cursos = Curso.objects.filter(camada__icontains=camada)
            print(cursos)

            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"

      #return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})


def leerProfesores(request):
    
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



def eliminarProfesor(request, profesor_nombre):
    
      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al menú
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)


def editarProfesor(request, profesor_nombre):
    
      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})

class CursoList(ListView):
    
      model = Curso 
      template_name = "AppCoder/cursos_list.html"

class CursoDetalle(DetailView):
    
      model = Curso
      template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
    
      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    
      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']

class CursoDelete(DeleteView):
    
      model = Curso
      success_url = "/AppCoder/curso/list"

#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "AppCoder/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
    
      return render(request, "AppCoder/login.html", {'form': form})

def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "AppCoder/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "AppCoder/registro.html", {"form": form})


# def logout_request(request):
#       logout(request)
#       messages.info(request, "Saliste sin problemas")
#       return redirect("inicio")

class CursoList(LoginRequiredMixin, ListView):
    
      model = Curso 
      template_name = "AppCoder/cursos_list.html"

# @login_required
# def inicio(request):

#       return render(request, "AppCoder/inicio.html")


@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppCoder/inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "AppCoder/inicio.html" ,{"url": avatares[0].imagen.url})
