from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class BaseManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extrafields):
        if not username:
            raise ValueError('Informe o usuário')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extrafields)

    def create_superuser(self, username, password, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)

        if extrafields.get('is_staff') is not True:
            raise ValueError('Precisa ser true')
        if extrafields.get('is_superuser') is not True:
            raise ValueError('Precisa ser true')

        return self._create_user(username, password, **extrafields)

class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(
        max_length=255, blank=False, null=False)

    status = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'email']
    objects = BaseManager()

    class Meta:
        db_table = 'user'
        

class List(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    class Meta:
        db_table = 'list'


class ListUsers(models.Model):
    id = models.AutoField(primary_key=True)
    id_list = models.ForeignKey(List, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    class Meta:
        db_table = 'list_users'
