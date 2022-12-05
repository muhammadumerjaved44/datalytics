import  courses.models as models
from rest_framework import serializers


# contact serializer class
class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = "__all__"

class CourseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseAuthor
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        fields = "__all__"

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Courses
        fields = "__all__"