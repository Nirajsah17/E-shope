from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def register(self):
        self.save()
