from enum import Enum

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from users.managers import UserManager


class UserRoles(Enum):
    """Классификатор ролей пользователя"""
    ADMIN = "admin"
    USER = "user"
    ROLES = ((ADMIN, "Администратор"), (USER, "Пользователь"))


class User(AbstractBaseUser):
    """Модель пользователя"""
    ADMIN = "admin"
    USER = "user"
    ROLES = ((ADMIN, "Администратор"), (USER, "Пользователь"))

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, max_length=50)
    # role = models.CharField(max_length=5, null=True, choices=UserRoles.ROLES, default=UserRoles.USER)
    role = models.CharField(max_length=5, null=True, choices=ROLES, default=USER)
    image = models.ImageField(upload_to="user_images/", null=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(null=True, default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    # Предопределение методов для корректной работы встроенной системы допуска и аутентификации пользователя
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # Переопределение менеджера объектов
    objects = UserManager()
