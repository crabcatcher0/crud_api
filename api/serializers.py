from rest_framework import serializers
from .models import BookList


class SerializedBook(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = ['id', 'book_name', 'author', 'description']
