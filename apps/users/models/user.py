from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  email = models.EmailField("Email", unique=True)

  USERNAME_FIELD = 'email'

  class Meta:
    db_table = 'users'
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'


class Role(models.Model):
  PERMISSION_CHOICES = [
    (0, 'Sin acceso')
    (1, 'Puede ver')
    (3, 'Puede ver y nmodificar')
  ]

  role_name = 
