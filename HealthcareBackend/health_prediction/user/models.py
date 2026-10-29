from django.db import models

# Create your models here.

class Patient(models.Model):
    full_name = models.CharField(max_length=200)

    dob = models.DateField()

    email = models.EmailField(unique=True)

    glucose = models.FloatField()

    haemoglobin = models.FloatField()

    cholesterol = models.FloatField()

    remarks = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "patient"

    def __str__(self):
        return self.full_name