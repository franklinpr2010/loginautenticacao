from django.db import models

# from django.contrib.auth.models import AbstractBaseUser
#Gerenciador do usuário e o usuário em si
from django.contrib.auth.models import AbstractUser, BaseUserManager

#Criou um gerador de usuário para um custom usuário de baixo, esse gerenciador é responsável por salvar, tanto o usuário comum como o gerenciador
class UsuarioManager(BaseUserManager):
    #esse vai ser o model de user que vai utilizar no banco de dados para autenticação, vai virar tabela no banco de dados
    use_in_migrations = True
    #email e senha para login e extra fields que pode ou não ter
    def _create_user(self, email, password, **extra_fields):
        #tornando o e-mail obrigatório porque vai logar com login e senha
        if not email:
            raise ValueError('O e-mail é obrigatório')
        #vai tirar a acentuação do email para um e-mail correto
        email = self.normalize_email(email)
        #o model do usuário passando o custon e-mail
        user = self.model(email=email, username=email, **extra_fields)
        #criptografa a senha
        user.set_password(password)
        #Salva o usuário
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        #o create user é um usuário comum, por isso o false, somente quando o is_staff está true que poderá ser setado
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        #se não for staff não consegue acessar a área administrativa
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    #USER NAME VAI SER O EMAIL
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email

    objects = UsuarioManager()




