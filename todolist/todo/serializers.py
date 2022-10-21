from rest_framework import serializers

from .models import Hero, Villain


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias' ,'desc')

class VillainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villain
        fields = ('name', 'alias','desc')