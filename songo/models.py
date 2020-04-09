from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    bio = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name

class Song(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    a_id=models.ManyToManyField(Artist)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    image=models.ImageField(upload_to="pics/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
    	return self.name

class Rating(models.Model):
	song=models.ForeignKey(Song, on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	class Meta:
		unique_together=(('user','song'),)
		index_together=(('user','song'),)

	def __str__(self):
		return self.rating