from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from PIL import Image
import PIL
# Create your models here.

class Post(models.Model):
	"""docstring for Post, represents an article """
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='defaultA.jpg',upload_to='profile_pics')
	category=models.CharField(default='Unspecified',max_length=100)
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = PIL.Image.open(self.image.path)
        #resizing image 
		if img.height >350 or img.width >350:
			outsize =(350,350)
			img.thumbnail(outsize)
			img.save(self.image.path)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})

	