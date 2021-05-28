from django.db import models


class Accinfo(models.Model):
    name = models.TextField()
    property = models.TextField()
    acc_id = models.TextField()
    acc_pw = models.TextField()

    def __str__(self):
        return self.name


