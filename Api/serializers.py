from rest_framework import serializers

from Api.models import Book


# manage serialization and deserialization from JSON
class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "description", "author")
