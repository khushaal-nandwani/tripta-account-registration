from django.db import models

class TForm(models.Model):
    email = models.EmailField(null=True, blank=True)
    client_code = models.IntegerField(blank=True , null=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.client_code


class Email(models.Model):
    admin_email = models.EmailField(null=True, blank=True)

