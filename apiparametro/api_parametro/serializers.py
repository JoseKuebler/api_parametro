from rest_framework import serializers
from .models import ParametroModel
class ParametroModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroModel
        fields = ["task", "completed", "timestamp", "updated", "user"]