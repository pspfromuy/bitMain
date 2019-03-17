from django.db import models

# Create your models here.
class Service(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True, null=True)
	image = models.ImageField(default='default.jpg', upload_to='service_pics') 
	url = models.URLField(blank=True, null=True)
	
	def __str__(self):
		return self.title