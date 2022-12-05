from django.contrib import admin
import courses.models as models
import images.models as images_models
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

    # def image_display(self, obj):
    #     return format_html('<img src="{}" width="auto" height="50px />'.format(obj.image.url))

    # image_display.short_description = 'image_display'

    list_display = [field.name for field in models.CourseCategoryImage._meta.fields]
    # list_display.append("image_display")
    list_filter = [field.name for field in models.CourseCategoryImage._meta.fields]



@admin.register(models.CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):

    # def image_display(self, instance):
    #     return format_html('<img src="{}" width="auto" height="50px />'.format(instance.thumbnail.coursecategoryimage.image.url))
    # image_display.short_description = 'image_display'

    # class CourseCatagoeryInline(admin.StackedInline):
    #     model = models.Course
    #     extra = 1

    # inlines = [
    #         CourseCatagoeryInline,
    #         ]

    # list_display = ["id", "name", "discription", "image_tag", "created_at", "updated_at"]#[field.name for field in models.CourseCategory._meta.fields]
    # readonly_fields = ["image_display"]
    list_display = [field.name for field in models.CourseCategory._meta.fields]
    list_filter = [field.name for field in models.CourseCategory._meta.fields]
    # list_display.append("image_display")




@admin.register(models.CourseInstructure)
class CourseInstructureAdmin(admin.ModelAdmin):

    def images(self, obj):
            html = '<a href="{url}" target="_blank"><img src="{url}" style="width: auto;height: 50px;" /></a>'
        return format_html(''.join(html.format(url=inst.image.url) for inst in obj.course_image.all()))


    list_display = [field.name for field in models.CourseInstructure._meta.fields]
    list_filter = list_display

class CourseImagesInline(admin.StackedInline):
    model = models.CourseImage
    extra = 0

class CourseCommentsInline(admin.StackedInline):
    model = models.CourseComments
    extra = 0

@admin.register(models.Course)
class CoursesAdmin(admin.ModelAdmin):


    inlines = [
            CourseImagesInline,
            CourseCommentsInline
            ]

    def images(self, obj):
        html = '<a href="{url}" target="_blank"><img src="{url}" style="width: auto;height: 50px;" /></a>'
        return format_html(''.join(html.format(url=inst.image.url) for inst in obj.course_image.all()))

    def comments(self, obj):
        html = '<a href="{}"<span/>{} | <b>{}</b></span></a>'
        return format_html(''.join(html.format(reverse('admin:comments_comment_change', args=(inst.id,)), inst.comment, inst.name) for inst in obj.course_comment.all()))

    images.short_description = 'images'
    comments.short_description = 'comments'


    list_display = [field.name for field in models.Course._meta.fields]
    list_filter = [field.name for field in models.Course._meta.fields]
    list_display.append("images")
    list_display.append("comments")
    readonly_fields = ('images',)

    # list_select_related = ('course_instructure', 'course_catagoery')
