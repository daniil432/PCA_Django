from django.db import models
from django.urls import reverse


class PatientFiles(models.Model):
    patient_type = models.CharField(max_length=4, help_text="Enter patient type here")
    patient_path = models.CharField(max_length=1000, help_text="Enter path to file location here")
    patient_number = models.IntegerField(help_text="Enter patient number here")

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.patient_type, self.patient_path

    def __int__(self):
        return self.patient_number
