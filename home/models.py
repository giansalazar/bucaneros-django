from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

# Create your models here.

class Personas(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apep = models.CharField(max_length=30, verbose_name="Apellido Paterno")
    apem = models.CharField(max_length=30, verbose_name="Apellido Materno")
    genero = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre + self.apep
    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

class Puestos(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"

class Empleados(models.Model):
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE, verbose_name="Persona")
    id_puesto = models.ForeignKey(Puestos, on_delete=models.CASCADE, verbose_name="Puesto")
    grado_estudios = models.CharField(max_length=40, verbose_name="Grado de Estudios")
    carrera = models.CharField(max_length=40)

    def __str__(self):
        return self.id_persona.nombre

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

class UsuarioManager(BaseUserManager):

    def _create_user(self, username, id_persona_id, telefono, email, is_active, is_staff, tipo_usuario, is_superuser, password):
        if not email:
            raise ValueError("El usuario debe tener un email")
        
        usuario = self.model(username=username, id_persona_id=id_persona_id, telefono=telefono, email=self.normalize_email(email), is_active=is_active, is_staff=is_staff, tipo_usuario=tipo_usuario, is_superuser=is_superuser)

        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario
    
    def create_user(self, username, id_persona_id, telefono, email, tipo_usuario, password=None):
        return self._create_user(username, id_persona_id, telefono, email, True, True, tipo_usuario, False, password)
    
    def create_superuser(self, username, id_persona_id, telefono, email, password):
        
        usuario=self.create_user(email,username=username, id_persona=id_persona_id, telefono=telefono, email=email, password=password)

        usuario.is_superuser=True

        usuario.save()

        return usuario
    

class Usuario(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(verbose_name="Usuario", max_length=20, unique=True)
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE, verbose_name="Persona")
    telefono =  models.CharField(max_length=10, verbose_name="Télefono")
    email = models.EmailField(verbose_name="Email")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    tipo_usuario = models.CharField(max_length=25)
    objects=UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'telefono','email','id_persona'

class usuarios_codigos(models.Model):
    codigo_reg = models.CharField(max_length=10)
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    estatus_reg = models.IntegerField(null=True)
    tipo_usuario = models.CharField(max_length=20,null=True)
