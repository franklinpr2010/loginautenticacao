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


























