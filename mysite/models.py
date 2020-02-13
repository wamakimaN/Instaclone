from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField(max_length = 30, blank = True)
  website = models.CharField(max_length=30, blank =True)
  phone_number = models.IntegerField(blank =True, null = True)
  location = models.CharField(max_length = 30, blank =True)
  birth_date = models.DateField(null =True, blank = True)
  profile_pic = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

  def __str__(self):
    return f'{self.user.username} Profile'

class Post(models.Model):
  profile = models.ForeignKey(Profile, null = True, blank = True)
  caption = models.CharField(max_length = 100)
  image = models.ImageField(upload_to='post_pics')
  posted_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.caption

class Comment(models.Model):
  post = models.ForeignKey(Post)
  user = models.ForeignKey(User)
  comment = models.CharField(max_length = 100)
  post_on = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
  post = models.ForeignKey(Post)
  user = models.ForeignKey(User)
