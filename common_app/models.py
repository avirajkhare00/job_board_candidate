from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PasswordUserMapping(models.Model):

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    random_string = models.CharField(max_length=256)

    def __str__(self):

        return self.user_id.username


class GoogleRecaptchaSiteKey(models.Model):

    config_id = models.IntegerField()
    secret_key = models.CharField(max_length=200)
    site_key = models.CharField(max_length=200)

    def __str__(self):

        return self.site_key


class GoogleRecaptchaPages(models.Model):

    config_id = models.IntegerField()
    page_name = models.CharField(max_length=100)

    def __str__(self):

        return self.page_name
