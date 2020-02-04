
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
