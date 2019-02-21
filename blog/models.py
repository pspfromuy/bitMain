from django.db import models

# Create your models here.
class service(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	