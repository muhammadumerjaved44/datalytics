from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ContactUsSerializer,
)
from rest_framework import status
from websites.models import ContactUs
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic.list import ListView


class HomeIndex(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'websites/index.html'

    def get(self, request, pk=None, format=None):
        # if pk is None:
        #     instance = Contact.objects.all()
        #     serializer = ContactSerializer(instance, many=True)
        #     return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # instance = get_object_or_404(Contact, id=pk)
        # serializer = ContactSerializer(instance)
        pass
        return Response({"stauts": "success", "data": "data"}, status=status.HTTP_200_OK)


# Contact form view
class ContactUsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = ContactUs.objects.all()
            serializer = ContactUsSerializer(instance, many=True)
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        instance = get_object_or_404(ContactUs, id=pk)
        serializer = ContactUsSerializer(instance)
        return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        # Update Section Instance

    def patch(self, request, pk, format=None):
        instance = get_object_or_404(ContactUs, id=pk)
        serializer = ContactUsSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = get_object_or_404(ContactUs, id=pk)
        serializer = ContactUsSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"stauts": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(ContactUs, id=pk)
        instance.delete()
        return Response(
            {"msg": "ContactUs deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )