from django.contrib import admin
import comments.models as models
import courses.models as courses_models
from django.contrib.auth.admin import UserAdmin




@admin.register(models.Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Comment._meta.fields]
    list_filter = list_display

    # class CourseInline(admin.StackedInline):
    #     model = courses_models.Course
    # extra = 1

    # inlines = [
    #         CourseInline,
    #         ]