from django.db import models

class Works(models.Model):
    person_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    salary=models.IntegerField(default=0)
    def __str__(self):
        return self.person_name

class Lives(models.Model):
    person_name=models.CharField(max_length=100)
    street=models.IntegerField()
    city=models.CharField(max_length=100)
    def __str__(self):
        return self.person_name