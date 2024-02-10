from django.db import models

class UserProfile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('', 'Select Gender'), ('Male', 'Male'), ('Female', 'Female')], blank=True)
    agree_terms = models.BooleanField()
    receive_newsletter = models.BooleanField()

    def __str__(self):
        return f"{self.fname} {self.lname}"

    class Meta:
        app_label = 'Domat'
