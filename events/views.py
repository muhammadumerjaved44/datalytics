from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import events.models as models
import events.serializers as serializers

class EventView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.Event.objects.all()
            serializer = serializers.EventSerializer(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.Event, id=pk)
        serializer = serializers.EventSerializer(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = serializers.EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Update Section Instance
    def patch(self, request, pk, format=None):
        instance = models.Event.objects.get(pk=pk)
        serializer = serializers.EventSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = models.Event.objects.get(pk=pk)
        serializer = serializers.EventSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        instance = models.Event.objects.get(pk=pk)
        instance.delete()
        return Response(
            {"msg": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )