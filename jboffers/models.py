from django.db import models

# Create your models here.
class JobOffers(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.CharField(max_length=50)
    job_title = models.CharField(max_length=30)
    job_description = models.CharField(max_length=50)
    salary = models.IntegerField()
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField()

    def __str__(self):
        return f'{self.company_name} {self.job_title}'



