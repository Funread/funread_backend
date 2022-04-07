from rest_framework import serializers
from BookCreator.models import BookCreator

class BookCreatorSerializer(serializers.ModelSerializer):
  class Meta:
    model = BookCreator
    fields = '__all__'
