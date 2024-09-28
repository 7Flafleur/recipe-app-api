"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from core.models import (
    Recipe,
    # Tag,
    # Ingredient,
)

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    # tags = TagSerializer(many=True, required=False)
    # ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe # REcipe model is going to use this serializer
        fields = [
            'id', 'title', 'time_minutes', 'price', 'link',

        ]
        read_only_fields = ['id']

# extension of the RecipeSerializer with added functionality
class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        #added fields
        fields = RecipeSerializer.Meta.fields + ['description']
