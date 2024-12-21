from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Product'

class Person(models.Model):
    SEX_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
    ]
    QUALIFICATION_CHOICES = [
        (1, 'High School'),
        (2, 'Associate Degree'),
        (3, "Bachelor's Degree"),
        (4, "Master's Degree"),
        (5, 'Doctorate'),
    ]
    YES_NO_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    id = models.IntegerField(primary_key=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.IntegerField(choices=SEX_CHOICES, null=True, blank=True)
    qualification = models.IntegerField(choices=QUALIFICATION_CHOICES, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    death = models.IntegerField(choices=YES_NO_CHOICES, null=True, blank=True)
    disability = models.IntegerField(choices=YES_NO_CHOICES, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Person'

from django.db import models

class Injection(models.Model):
    DRUG_CHOICES = [
        (1, 'One-Time High-Risk Injection (Emergency)'),
        (2, 'Routine Injections (Multiple)'),
        (3, 'One-Time Injection (Non-Emergency)'),
    ]

    INJECTION_TYPE_CHOICES = [
        (1, 'INJECTION, SOLUTION'),
        (2, 'Capsule'),
        (3, 'Dry Powder'),
        (4, 'Solution for injection in pre-filled pen'),
        (5, 'Solution for injection in pre-filled syringe'),
    ]

    id = models.IntegerField(primary_key=True)
    drug = models.IntegerField(choices=DRUG_CHOICES, null=True, blank=True)  # The second column for injection type
    injection = models.IntegerField(choices=INJECTION_TYPE_CHOICES, null=True, blank=True)  # Third column for description

    class Meta:
        managed = False
        db_table = 'Injection'



