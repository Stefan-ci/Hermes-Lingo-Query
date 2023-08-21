from django.db import models
from secrets import token_urlsafe
from random import choice as random_choice
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


AVATARS = [
    "assets/avatars/avatar_cat.png",
    "assets/avatars/avatar_dog.png",
    "assets/avatars/avatar_leopard.png",
]


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Email address required!")

        if not username:
            raise ValueError("Username required!")
        
        if not first_name:
            raise ValueError("First name required!")
        
        if not last_name:
            raise ValueError("Last name required!")
        
        if self.filter(email=str(email).lower()).exists():
            raise ValueError("Email address is already in use")
        
        if self.filter(username=str(username).lower()).exists():
            raise ValueError("Username is already in use")
        
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False, editable=False)
    is_active = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False, editable=False)
    is_superuser = models.BooleanField(default=False, editable=False)
    api_key = models.CharField(max_length=500, unique=True, default=token_urlsafe(32), editable=False)
    avatar = models.ImageField(upload_to="users/avatars/%Y/%m/", blank=True, null=True, default=random_choice(AVATARS))
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    
    objects = UserManager()
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined", "username", "email"]


    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    def full_name(self) -> str:
        """ Return first_name + last_name """
        return f"{self.first_name} {self.last_name.upper()}"
