
from .models import Course, CourseInstructure, CourseCategory, CourseImage, CourseCategoryImage
from rest_framework import serializers


class CourseInstructureSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseInstructure
        fields = "__all__"



class CourseImageSerializer(serializers.ModelSerializer):


    class Meta:
        model = CourseImage
        fields = "__all__"

class CourseCategoryImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCategoryImage
        fields = "__all__"


class CourseCategorySerializer(serializers.ModelSerializer):

    # course_catagoery_image = CourseCategoryImageSerializer(many=False, required=False, allow_null=True)
    class Meta:
        model = CourseCategory
        fields = "__all__"
class CourseSerializer(serializers.ModelSerializer):

    course_instructure = CourseInstructureSerializer(many=False, required=False, allow_null=True)
    course_catagoery = CourseCategorySerializer(many=False, required=False, allow_null=True)
    course_image = CourseImageSerializer(many=True)


    class Meta:
        model = Course
        fields = [
            "id", "name", "course_code", "course_mode", "discription", "created_at", "updated_at", "course_catagoery", "course_instructure", "course_image",
        ]
        # fileds = "__all__"
