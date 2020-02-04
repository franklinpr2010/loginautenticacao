#Formulário de criação e alteração de usuário
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#vai obter o custom usuário
from .models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        #custom usuário é modelo dele
        model = CustomUsuario
        #Campos necessário para esse formulario, vai colocar esses campos nos formulários
        fields = ('first_name', 'last_name', 'fone')
        #Deixar claro que o username é o e-mail
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        #averiguando se o password é igual para depois criptografar
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        #Se commit tiver como true
        if commit:
            user.save()
        return user

#formulário de alteração do usuário
class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')

