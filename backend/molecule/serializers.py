from rest_framework import serializers

from molecule.models import Molecule, Activity, Target


class MoleculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = '__all__'


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    target = TargetSerializer()

    class Meta:
        model = Activity
        fields = '__all__'
