from django.db import models


class Birthdays(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = "Birthdays"
