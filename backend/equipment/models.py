from django.db import models

class UploadHistory(models.Model):
    total_equipment = models.IntegerField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()
    type_distribution = models.JSONField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload at {self.uploaded_at}"
