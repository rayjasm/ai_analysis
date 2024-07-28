from django.db import models

class AiAnalysisLog(models.Model):
    id = models.IntegerField(primary_key=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)
    success = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    returnclass = models.IntegerField(null=True, blank=True)
    confidence = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)
    request_timestamp = models.IntegerField(null=True, blank=True)
    response_timestamp = models.IntegerField(null=True, blank=True)
