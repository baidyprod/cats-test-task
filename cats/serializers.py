from rest_framework import serializers

from .models import Mission, SpyCat, Target
from .validators import validate_cat_breed


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ["id", "name", "years_of_experience", "breed", "salary", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def validate_breed(self, value):
        if not validate_cat_breed(value):
            raise serializers.ValidationError(f"Breed '{value}' is not a valid cat breed.")
        return value


class SpyCatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ["salary"]


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "country", "notes", "is_complete", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class TargetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["notes", "is_complete"]

    def validate(self, data):
        target = self.instance
        if target.is_complete and "notes" in data:
            raise serializers.ValidationError("Cannot update notes on a completed target.")
        if target.mission.is_complete and "notes" in data:
            raise serializers.ValidationError("Cannot update notes on a target of a completed mission.")
        return data


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)
    cat_name = serializers.CharField(source="cat.name", read_only=True, allow_null=True)

    class Meta:
        model = Mission
        fields = ["id", "cat", "cat_name", "is_complete", "targets", "created_at", "updated_at"]
        read_only_fields = ["is_complete", "created_at", "updated_at"]

    def validate_targets(self, value):
        if len(value) < 1 or len(value) > 3:
            raise serializers.ValidationError("A mission must have between 1 and 3 targets.")
        return value

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        mission = Mission.objects.create(**validated_data)

        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)

        return mission


class MissionAssignCatSerializer(serializers.Serializer):
    cat_id = serializers.IntegerField()

    def validate_cat_id(self, value):
        try:
            cat = SpyCat.objects.get(id=value)
        except SpyCat.DoesNotExist:
            raise serializers.ValidationError("Cat does not exist.") from None

        # Check if cat already has an active mission
        if Mission.objects.filter(cat=cat, is_complete=False).exists():
            raise serializers.ValidationError("Cat is already assigned to an active mission.")

        return value
