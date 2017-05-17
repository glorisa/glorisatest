from django.db import models

class contact(models.Model):
    name = models.CharField(null=False, max_length=50)
    email = models.EmailField(null=False)
    company = models.CharField(null=False, max_length=500, default='company')
    phone = models.CharField(null=False, max_length=20)
    subject = models.CharField(null=False, max_length=500)
    message = models.TextField(null=False)

    def __str__(self):
        return self.name + '-' + self.subject


class team(models.Model):
    name = models.CharField(null=False, max_length=50)
    about = models.TextField(null=False)
    slug = models.TextField(null = True)
    leader = models.BooleanField(default=False)
    photo = models.CharField(max_length=2000)

    def __str__(self):
        return  self.name

