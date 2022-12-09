from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import clients.models as models
import clients.serializers as serializers







class ClientsView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.Clients.objects.all()
            serializer = serializers.ClientsSerializer(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(models.Clients, id=pk)
        serializer = serializers.ClientsSerializer(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = serializers.ClientsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Update Section Instance
    def patch(self, request, pk, format=None):
        instance = models.Clients.objects.get(pk=pk)
        serializer = serializers.ClientsSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = models.Clients.objects.get(pk=pk)
        serializer = serializers.ClientsSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        instance = models.Clients.objects.get(pk=pk)
        instance.delete()
        return Response(
            {"msg": "contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )