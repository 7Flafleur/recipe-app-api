"""
Serializers for the API view
"""
from django.conctib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ Serializer (takes and validates JSON input and converts it
    to a Python object or database model) for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['email','password','name']
        extra_kwargs = {'password' : {'write_only': True,'min_length':5}}

    def create(self,validated_data):
        """ Create and return a user with encrypted password.
        Overrides serialize behaviour(save password as cleartext).
        Will only be called after successfull validation"""
        return get_user_model().objects.create_user(**validated_data)
