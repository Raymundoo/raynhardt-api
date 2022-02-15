from rest_framework import serializers
from mascotas.models import Mascota, Persona, Vacuna


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'


class VacunaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacuna
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer()
    vacunas = VacunaSerializer(many=True)

    class Meta:
        model = Mascota
        fields = '__all__'
