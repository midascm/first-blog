from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bookmark(models.Model):
    name = models.CharField('NAME', max_length=100, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bookmark:bookmark_detail', args=(self.id,))


class Marklist(models.Model):
    book = models.ForeignKey(Bookmark,on_delete=models.CASCADE)
    title = models.CharField('title', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookmark:marklist_detail', args=(self.id,))
