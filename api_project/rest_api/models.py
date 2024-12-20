from django.db import models

# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class DataPoint(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    operator = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    lat = models.FloatField()
    lon = models.FloatField()
    elevation = models.FloatField()
    temp = models.FloatField()
    description = models.TextField()
    operator_inspection = models.BooleanField(default=False)

    
    class Meta:
        ordering = ['created']