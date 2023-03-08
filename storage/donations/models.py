from django.db import models

# Create your models here.
class Storage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    size = models.IntegerField(default=55, null=True)

    def __str__(self):
        return self.name