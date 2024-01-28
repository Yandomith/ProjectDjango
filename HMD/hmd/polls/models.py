from django.db import models

# Create your models here.
class Users(models.Model):
    fName= models.CharField(max_length = 20)
    mName= models.CharField(max_length = 20, default='', blank=True)
    lName = models.CharField(max_length = 20)
    Email = models.EmailField(max_length = 50)
    Password = models.CharField(max_length = 15)

class Categories(models.Model):

    categoriesName = models.CharField(max_length = 20)

class Post(models.Model):
    postName = models.CharField(max_length=50)
    postBio = models.CharField(max_length = 200)
    postDate = models.DateTimeField("date published")
    postPrice = models.IntegerField(default = 0)
    postBy = models.ForeignKey(Users, on_delete=models.CASCADE)
    postTag = models.ForeignKey(Categories, on_delete=models.CASCADE)
    postDescription = models.CharField(max_length = 1000)
    postLike= models.IntegerField(default = 0)
    postRate = models.IntegerField(default = 0 )
    

