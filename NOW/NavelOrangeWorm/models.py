from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    content = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    # Returns the string representation of the model.
    def __str__(self):
        return self.name
