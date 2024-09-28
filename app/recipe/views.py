"""
Views for the recipe APIs
"""

from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    # Tag,
    # Ingredient,
)
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):  # ModelViewset designed to work with db models
    """View for manage recipe APIs.""" # Docstrings are displayed in Swagger Doc
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all() #specifies which models to use
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]




    # override getqueryset method to get objects
    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        # tags = self.request.query_params.get('tags')
        # ingredients = self.request.query_params.get('ingredients')
        queryset = self.queryset
        # if tags:
        #     tag_ids = self._params_to_ints(tags)
        #     queryset = queryset.filter(tags__id__in=tag_ids)
        # if ingredients:
        #     ingredient_ids = self._params_to_ints(ingredients)
        #     queryset = queryset.filter(ingredients__id__in=ingredient_ids)

        return queryset.filter(
            user=self.request.user
        ).order_by('-id').distinct()

    def get_serializer_class(self):
        """Return the serializer class for request type."""
        if self.action == 'list': #request to root url that shows all recipes
            return serializers.RecipeSerializer
        elif self.action == 'upload_image':
            return serializers.RecipeImageSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        #overrides behaviour of how Django saves model in a viewset
        """Create a new recipe."""
        #set user variable to current authenticated user
        serializer.save(user=self.request.user)