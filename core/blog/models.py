from django.db import models
from django.contrib.auth import get_user_model

# getting user model
User = get_user_model()

class Post(models.Model):
  """
  this is a post model for blog app
  """
  author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
  title = models.CharField(max_length=250)
  image = models.ImageField(null=True, blank=True)
  content = models.TextField()
  status = models.BooleanField()
  category = models.ForeignKey("Category",null=True, on_delete=models.SET_NULL)

  created_at = models.DateTimeField(auto_now_add=True) # when we make a record it will sets
  updated_at =  models.DateTimeField(auto_now=True) # on any changes sets again
  published_at = models.DateTimeField()

  def __str__(self):
    return self.title

class Category(models.Model):
  title = models.CharField(max_length=250)

  def __str__(self):
    return self.title

