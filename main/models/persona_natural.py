from django.db import models


class PersonaNatural(models.Model):
    ci = models.CharField(max_length=11, unique=True)

    class Meta:
        verbose_name = 'Persona Natural'
        verbose_name_plural = 'Personas Naturales'

    def __str__(self):
        return self.ci
