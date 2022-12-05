from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid
from comments.models import Comment
from images.models import Image

# create contact us model

class InstructureImage(Image):
    pass



class CourseCategory(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name



class CourseCategoryImage(Image):
    course_catagoery = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)

class CourseInstructure(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True
    )
    discription = models.TextField(blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    facebook_link = models.CharField(max_length=255, blank=True, null=True)
    linkedin_link = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)
    twitter_link = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.ForeignKey(InstructureImage, blank=True, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

class Course(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_catagoery = models.ForeignKey(
        CourseCategory, on_delete=models.DO_NOTHING, related_name="course_catagoery", null=True, blank=True
    )
    course_instructure = models.ForeignKey(CourseInstructure, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    course_code = models.CharField(max_length=255, blank=True, null=True)
    course_mode = models.CharField(max_length=255, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourseImage(Image):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
