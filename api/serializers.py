from rest_framework import serializers
from api.models import MrOlimpya

class MrOlimpyaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MrOlimpya  
        exclude = ['is_removed', 'created', 'modified']