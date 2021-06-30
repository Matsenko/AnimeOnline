from rest_framework import serializers
from .models import Anime_list
class AnimeSerializer(serializers.Serializer):
    anime_name = serializers.CharField(max_length=200)
    anime_text = serializers.CharField()
    pub_date = serializers.DateTimeField()
    def create(self, validated_data):
        return Anime_list.objects.create(**validated_data)    
    def update(self, instance, validated_data):
        instance.anime_name = validated_data.get('anime_name', instance.anime_name)
        instance.anime_text = validated_data.get('anime_text', instance.anime_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance        