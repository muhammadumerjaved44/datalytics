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
import websites.serializers as websites_serializers
import courses.models as courses_models
import events.models as events_models
import clients.models as clients_models
import courses.serializers as courses_serializers
import events.serializers as events_serializers
import clients.serializers as clients_serializers

class HomeIndex(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'websites/index.html'

    def get(self, request, pk=None, format=None):
        course_raw =  courses_models.Course.objects.all()
        courses = courses_serializers.CourseSerializer(course_raw, many=True)

        events_raw =  events_models.Event.objects.all()
        events = events_serializers.EventSerializer(events_raw, many=True)

        clients_raw =  clients_models.Clients.objects.all()
        clients = clients_serializers.ClientsSerializer(clients_raw, many=True)

        context = {}
        context['courses'] = courses.data
        context["events"] = events.data
        context["clients"] = clients.data


        return Response({"stauts": "success", "data": context}, status=status.HTTP_200_OK)

# def index(request):
#     if request.method== "GET":
#         courses_list = courses_models.Course.objects.all()
#         course_images = course

#         context = {}

#         # add the dictionary during initialization
#         context["data"] = courses_list

#         return render(request, "websites/index.html", context)


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