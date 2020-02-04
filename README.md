# loginautenticacao
Autenticação e Login no Python  
Criando um Custom User Model  
Criando uma tela de autenticação que não seja essa que o Django forneça por default  

Instalar o Django:
pip install django

Criar projeto Python:
django-admin startproject loginautenticacao .

Criar Aplicação Usuarios:
django-admin startapp usuarios

A área administrativa do Django vem por default o nome do usuário no login, muitas vezes se quer configurar o email, o cpf como  login do usuário.

Rodar o comando makemigrations = python manage.py makemigrations

Rodar o comando migrate = python manage.py migrate para criar as tabelas

Rodar o comando create super user = python manage.py createsuperuser, para criar as tabelas, vai aparecer exatmente como colocou no model.


Alterar o admin.py



#No admin que vai criar o usuário
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    #formulário de adição
    add_form = CustomUsuarioCreateForm
    #formulário de alteração
    form = CustomUsuarioChangeForm
    #model vai ser o custom usuário
    model = CustomUsuario
    # o list display vai ser dessa forma
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # Quer apresentar nos campos email e password
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        #Usuário logou pela ultima vez, quando o usuário foi cadastrado no sistema
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


Acessar o runserver: python manage.py runserver



Aqui são as rotas do admin:


>python manage.py shell
Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 01:54:44) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.urls import get_resolver
>>> from pprint import pprint
>>> ppprint(get_resolver().url_patterns[0].url_patterns)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'ppprint' is not defined
>>> pprint(get_resolver().url_patterns[0].url_patterns)
[<URLPattern '' [name='index']>,
 <URLPattern 'login/' [name='login']>,
 <URLPattern 'logout/' [name='logout']>,
 <URLPattern 'password_change/' [name='password_change']>,
 <URLPattern 'password_change/done/' [name='password_change_done']>,
 <URLPattern 'jsi18n/' [name='jsi18n']>,
 <URLPattern 'r/<int:content_type_id>/<path:object_id>/' [name='view_on_site']>,
 <URLResolver <URLPattern list> (None:None) 'auth/group/'>,
 <URLResolver <URLPattern list> (None:None) 'usuarios/customusuario/'>,
 <URLPattern '^(?P<app_label>auth|usuarios)/$' [name='app_list']>]
     
     
Criar as paginas base.html, index.html e login.html  
 
No settings.py, quando der logout redirecionar para o index  
 
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

Em urls.py  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    #vai para a pagina index
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

     
 
 
     
  
 


























