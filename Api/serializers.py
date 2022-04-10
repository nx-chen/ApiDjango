from rest_framework import serializers
from Api.models import Book


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id',
                  'title',
                  'description',
                  'author')
