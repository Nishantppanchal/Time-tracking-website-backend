from django.db import models
from django.contrib.auth.base_user import (
    AbstractBaseUser, BaseUserManager
)
from django.db.models.fields import EmailField

# Create your models here.


class userManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        first_name = first_name[0].upper() + first_name[1:].lower()
        last_name = last_name[0].upper() + last_name[1:].lower()
        user = self.model(email=email,first_name=first_name, last_name=last_name, is_active=False, is_staff=False)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        first_name = first_name[0].upper() + first_name[1:].lower()
        last_name = last_name[0].upper() + last_name[1:].lower()
        user = self.model(email=email,first_name=first_name, last_name=last_name, is_active=True, is_staff=True)
        user.set_password(password)
        user.save()
        return user
    
class users(AbstractBaseUser):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = userManager()
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['firstName', 'lastName', 'email']
    