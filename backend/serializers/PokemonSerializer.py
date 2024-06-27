from rest_framework import serializers
from backend.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'pokedex_number', 'primary_type', 'secondary_type', 'image']

    def create(self, validated_data):
        image = validated_data.pop('image', None)

        pokemon = Pokemon.objects.create(**validated_data)

        if image:
            pokemon.image.save(image.name, image)

        return pokemon

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.pokedex_number = validated_data.get('pokedex_number', instance.pokedex_number)
        instance.primary_type = validated_data.get('primary_type', instance.primary_type)
        instance.secondary_type = validated_data.get('secondary_type', instance.secondary_type)

        image = validated_data.get('image', None)
        if image:
            instance.image.save(image.name, image)

        instance.save()
        return instance