from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class job(models.Model):
    SIZE_1_9 = 'size_1-9'
    SIZE_10_49 = 'size_10-49'
    SIZE_50_99 = 'size_50-99'
    SIZE_100 = 'size_100'
    partiel = 'partiel'
    plein = 'plein'
    stage = 'stage'
    freelance = 'freelance'

    CHOICES_SIZE = (
        (SIZE_1_9, '1-9'),
        (SIZE_10_49, '10-49'),
        (SIZE_50_99, '50-99'),
        (SIZE_100, '100+'),
    )

    CHOICES_CONTRAT = (
        (partiel, 'partiel'),
        (plein, 'plein'),
        (stage, 'stage'),
        (freelance, 'freelance'),
    )

    moins_de_5oo = 'moins_de_5oo'
    s500_1000 = '500-1000'
    s1000_1500= '1000-1500'
    s2000_2500 =  '2000-2500'
    s2500_3000 = '2500-3000'
    s3000 = '3000+'




    SALARY = (
        (moins_de_5oo, 'moins_de_5oo'),
        (s500_1000, '500-1000'),
        (s1000_1500, '1000-1500'),
        (s2000_2500, '2000-2500'),
        (s2500_3000, '2500-3000'),
        (s3000, '3000+'),
    )

    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)

    company_name = models.CharField(max_length=255)
    company_adress = models.CharField(max_length=255, null=True, blank=True)
    company_zipcode = models.CharField(max_length=255, null=True, blank=True)
    company_place = models.CharField(max_length=255, null=True, blank=True)
    company_country = models.CharField(max_length=255, null=True, blank=True)
    company_size = models.CharField(max_length=20, choices=CHOICES_SIZE, default=SIZE_1_9)
    company_contrat = models.CharField(max_length=20, choices= CHOICES_CONTRAT, default=plein)
    company_salary = models.CharField(max_length=20, choices= SALARY, default=s500_1000)

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    