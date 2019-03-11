from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PasswordUserMapping(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    random_string = models.CharField(max_length=256)

    def __str__(self):

        return self.user_id.username