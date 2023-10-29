from django.db import models


# Create your models here.
class Writer(models.Model):
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.last_name)


class Genre(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.type)


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('Writer', on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    genre = models.ForeignKey('Genre',on_delete=models.SET_NULL,null=True)
    release_date = models.IntegerField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return str(self.id) +' ' +'by' + ' ' +str((self.author))+ ' ' + '-' + ' '+  str(self.release_date)
