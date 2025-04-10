from rest_framework import serializers
from .models import Version, Testament, Book, Verse

class VersionSerializer(serializers.ModelSerializer):

        name = serializers.CharField(required=False)
        language = serializers.CharField(required=False)

        class Meta:
             model = Version
             fields = '__all__'

class TestamentSerializer(serializers.ModelSerializer):
     
     class Meta:
         model = Testament
         fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
     
     class Meta:
         model = Book
         fields = '__all__'
        
class VerseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verse
        fields = '__all__'