from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
  """
  this Model is for Managing New User Model
  """
  def create_user(self, email, password, **kwargs):
    if not email :
        raise ValueError(_("email must be set"))
    email = self.normalize_email(email)
    user = self.model(email=email, **kwargs)
    user.set_password(password) # set the password for user
    user.save()
    return user

  def create_superuser(self, email, password, **kwargs):
    """
    method for creating super users
    """
    kwargs.setdefault("is_staff", True)
    kwargs.setdefault("is_active", True)
    kwargs.setdefault("is_superuser", True)

    if kwargs.get("is_staff") is not True:
        raise ValueError(_("Superuser must have is_staff = True"))
    if kwargs.get("is_superuser") is not True:
        raise ValueError(_("Superuser must have is_superuser = True"))
    if kwargs.get("is_active") is not True:
        raise ValueError(_("Superuser must be active"))

    return self.create_user(email=email, password=password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
  """
  this model is For Rebuilding default User Model in Django
  """
  email = models.EmailField(unique=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  # is_verified = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  create_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  def __str__(self):
    return self.email


class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  image = models.ImageField(blank=True, null=True)
  description = models.TextField()

  create_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.email

@receiver(post_save, sender=User) # any time that a model changes that send a signal
def save_profile(sender, instance, created, **kwarge):
  if created:
    Profile.objects.create(user=instance)