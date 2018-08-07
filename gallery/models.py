from datetime import datetime
from django.db import models

# Create your models here.
class Images(models.Model):
    imgsrc = models.TextField()
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Images"
