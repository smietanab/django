from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length = 32)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ['-timestamp']

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
   
   

class Author(models.Model):
    name = models.CharField(max_length = 100)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ManyToManyField(Author)
    length = models.IntegerField()
    
class SmithBook(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author, limit_choices_to = {'name_endswith' : 'Smith'})
#admin.site.register(BlogPost)
admin.site.register(BlogPost,BlogPostAdmin)