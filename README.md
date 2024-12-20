# Django-Rest-Framework-API-
Add objects to djagno rest framework

from rest_api.models import DataPoint
from rest_api.serializers import DataPointSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

datapoint = DataPoint(operator='name', title='Engineer', lat=12.43, lon=34.57, elevation=4324.5, temp=12.52, description='Software Project',operator_inspection=True)

datapoint.save()
