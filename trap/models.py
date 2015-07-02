__author__ = 'sunde'
from django.db import models

class req_records(models.Model):
    req_date = models.DateTimeField("Date of request")
    rem_ip = models.GenericIPAddressField("Field for IP adresses")
    req_method = models.CharField(max_length=20)
    scheme = models.CharField(max_length=10)
    query_string = models.TextField()
    query_parameters = models.TextField()
    cookies = models.TextField()
    headers = models.TextField()