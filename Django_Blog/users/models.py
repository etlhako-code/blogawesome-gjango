from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
import PIL
# Create your models here.

class Profile(models.Model):
	"""docstring for Profile"""
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = PIL.Image.open(self.image.path)
		#image resizing
		if img.height >350 or img.width >350:
			outsize =(350,350)
			img.thumbnail(outsize)
			img.save(self.image.path)

