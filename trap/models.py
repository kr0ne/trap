from django.db import models


class ReqRecords(models.Model):
    req_date = models.DateTimeField("Date of request")
    rem_ip = models.GenericIPAddressField("Field for IP addresses")
    req_method = models.CharField(max_length=20)
    scheme = models.CharField(max_length=10)
    query_string = models.TextField()
    query_parameters = models.TextField()
    cookies = models.TextField()
    headers = models.TextField()


class Traps(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField("Creation time of the trap")
    name = models.CharField(max_length=30)
