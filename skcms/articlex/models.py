from django.db import models

class Article(models.Model):
	title = models.CharField(max_length = 100, verbose_name ="tytul")
	content = models.TextField(verbose_name = "Zawartosc")
	published = models.DateTimeField(verbose_name = "Data publikacji")
	
	def __unicode__(self):
		return self.title
