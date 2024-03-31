from rest_framework import serializers

from .models import Resource

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id',
            'anon_title',
            'media_type',
            'duration',
            'pub_date',
            'public',
        ]
