from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'BusNo', 'BusRoute', 'latitude', 'longitude',  'time' )

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.BusNo = validated_data.get('BusNo', instance.title)
        instance.BusRoute = validated_data.get('BusRoute', instance.code)
        instance.latitude = validated_data.get('latitude', instance.linenos)
        instance.longitude = validated_data.get('longitude', instance.language)
        instance.time = validated_data.get('time', instance.time)
        instance.save()
        return instance
