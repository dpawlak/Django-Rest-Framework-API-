from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_api.models import DataPoint, LANGUAGE_CHOICES, STYLE_CHOICES

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DataPointSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    operator = serializers.CharField(required=False, allow_blank=True, max_length=100)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)
    elevation = serializers.FloatField(required=True)
    temp = serializers.FloatField(required=True)
    description = serializers.CharField(required=False)
    operator_inspection = serializers.BooleanField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return DataPoint.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.operator = validated_data.get('operator', instance.operator)
        instance.title = validated_data.get('title', instance.title)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.elevation = validated_data.get('elevation', instance.elevation)
       	instance.temp = validated_data.get('temp', instance.temp)

        instance.description = validated_data.get('description', instance.description)

        instance.operator_inspection = validated_data.get('operator_inspection', instance.operator_inspection)
        instance.save()
        return instance