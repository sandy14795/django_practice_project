from django.db import models
from datetime import datetime
# Create your models here.


class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length = 200)
	category_summary = models.CharField(max_length = 200)
	category_slug = models.CharField(max_length = 200)

	class Meta:
		verbose_name_plural = "Categories"  #This is just for admin panel

	def __str__(self):
		return self.tutorial_category	

class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length = 200)
	tutorial_category = models.ForeignKey(TutorialCategory, verbose_name = 'Category',
										  default=1, on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length = 200)

	class Meta:
		verbose_name_plural = "Series"  #This is just for admin panel

	def __str__(self):
		return self.tutorial_series

class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField() #something of not finite length
	tutorial_published = models.DateTimeField("date published", default = datetime.now())
	tutorial_series = models.ForeignKey(TutorialSeries, verbose_name = 'Series', # blank = True, null = True,on_delete=models.CASCADE)
										  default=1, on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length = 200, default = 1)

	def __str__(self):
		return self.tutorial_title
