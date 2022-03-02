from rest_framework import serializers
from whatthefuck.models import *

class WhatTheFuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatTheFuck
        fields = ['id', 'name']

    def create(self, validated_data):
        """
        Create and return a new `WhatTheFuck` instance, given the validated data.
        """
        return WhatTheFuck.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `WhatTheFuck` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance