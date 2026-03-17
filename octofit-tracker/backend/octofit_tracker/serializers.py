"""Serializers for the OctoFit Tracker API.

This module contains helper fields/serializers that are aware of MongoDB ObjectId fields.
"""

from bson import ObjectId
from rest_framework import serializers


class ObjectIdField(serializers.Field):
    """A serializer field that (de)serializes MongoDB ObjectIds as strings."""

    def to_representation(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

    def to_internal_value(self, data):
        if data in (None, ''):
            return None
        try:
            return ObjectId(str(data))
        except Exception as exc:
            raise serializers.ValidationError('Invalid ObjectId') from exc
