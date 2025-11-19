from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Mission, SpyCat, Target
from .serializers import (
    MissionAssignCatSerializer,
    MissionSerializer,
    SpyCatSerializer,
    SpyCatUpdateSerializer,
    TargetUpdateSerializer,
)


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def get_serializer_class(self):
        if self.action == "partial_update":
            return SpyCatUpdateSerializer
        return SpyCatSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.cat is not None:
            return Response({"error": "Cannot delete a mission assigned to a cat."}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=["patch"])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
        serializer = MissionAssignCatSerializer(data=request.data)

        if serializer.is_valid():
            cat = SpyCat.objects.get(id=serializer.validated_data["cat_id"])
            mission.cat = cat
            mission.save()
            return Response(MissionSerializer(mission).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["patch"], url_path="targets/(?P<target_id>[^/.]+)")
    def update_target(self, request, pk=None, target_id=None):
        mission = self.get_object()
        target = get_object_or_404(Target, mission=mission, id=target_id)

        serializer = TargetUpdateSerializer(target, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            # Check if mission should be auto-completed
            mission.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
