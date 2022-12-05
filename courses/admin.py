from django.contrib import admin
import courses.models as models
from django.utils.html import format_html
from django.urls import reverse


@admin.register(models.InstructureImage)
class InstructureImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.InstructureImage._meta.fields]
    list_filter = list_display

@admin.register(models.CourseImage)
class CourseImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.CourseImage._meta.fields]

    # class CourseInline(admin.StackedInline):
    #     model = models.Course
    #     extra = 1

    # inlines = [
    #         CourseInline,
    #         ]

@admin.register(models.CourseCategoryImage)
class CourseCategoryImageAdmin(admin.ModelAdmin):

    def image_display(self, obj):
        return format_html('<img src="{}" width="auto" height="50px />'.format(obj.image.url))

    image_display.short_description = 'image_display'

    list_display = [field.name for field in models.CourseCategoryImage._meta.fields]
    list_display.append("image_display")
    list_filter = [field.name for field in models.CourseCategoryImage._meta.fields]



@admin.register(models.CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):

    def image_display(self, instance):
        return format_html('<img src="{}" width="auto" height="50px />'.format(instance.thumbnail.coursecategoryimage.image.url))
    image_display.short_description = 'image_display'

    # class CourseCatagoeryInline(admin.StackedInline):
    #     model = models.Course
    #     extra = 1

    # inlines = [
    #         CourseCatagoeryInline,
    #         ]

    # list_display = ["id", "name", "discription", "image_tag", "created_at", "updated_at"]#[field.name for field in models.CourseCategory._meta.fields]
    readonly_fields = ["image_display"]
    list_display = [field.name for field in models.CourseCategory._meta.fields]
    list_filter = [field.name for field in models.CourseCategory._meta.fields]
    list_display.append("image_display")




@admin.register(models.CourseInstructure)
class CourseInstructureAdmin(admin.ModelAdmin):

    def image_display(self, instance):
        return format_html('<img src="{}" width="50px" height="50px />'.format(instance.thumbnail.image.url))

    image_display.short_description = 'image_display'
    list_display = [field.name for field in models.CourseInstructure._meta.fields]
    list_filter = list_display




@admin.register(models.Course)
class CoursesAdmin(admin.ModelAdmin):
    # def image_display(self, objs):
    #     rel_list = "<ol>"
    #     for obj in objs.thumbnails.prefetch_related():
    #         link = reverse("admin:images_image_change", args=[obj.id])
    #         rel_list += f"<li><a href='{link}'><img src='{obj.image.url}' width='50px' height='50px' /></a></li>"
    #     rel_list += "</ol>"
    #     return format_html(rel_list)

    # image_display.short_description = 'image_display'


    list_display = [field.name for field in models.Course._meta.fields]
    list_filter = [field.name for field in models.Course._meta.fields]
    # list_display.append("image_display")

    list_select_related = ('course_instructure', 'course_catagoery')
