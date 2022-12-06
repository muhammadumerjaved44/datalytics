from django.contrib import admin
import courses.models as models
import images.models as images_models
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode


# @admin.register(models.InstructureImage)
# class InstructureImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in models.InstructureImage._meta.fields]
#     list_filter = list_display

# @admin.register(models.CourseImage)
# class CourseImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in models.CourseImage._meta.fields]
#     list_filter = list_display


# @admin.register(models.CourseCategoryImage)
# class CourseCategoryImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in models.CourseCategoryImage._meta.fields]
#     list_filter = [field.name for field in models.CourseCategoryImage._meta.fields]



@admin.register(models.CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):

    class CourseCategoryImageInline(admin.StackedInline):
        model = models.CourseCategoryImage
        extra = 0

    class CourseInline(admin.TabularInline):
        model = models.Course
        extra = 0

    inlines = [
            CourseCategoryImageInline,
            CourseInline
            ]

    def images(self, obj):
        html = '<a href="{url}" target="_blank"><img src="{url}" style="width: auto;height: 50px;" /></a>'
        return format_html(''.join(html.format(url=inst.image.url) for inst in obj.course_catagoery_image.all()))

    def recent_courses(self, objs):
        instances = objs.course_catagoery.all()
        if len(instances) >= 5:
            instances = instances[-5]
        html = "<ul>"
        for obj in instances:
            link = (reverse("admin:courses_course_changelist")  + "?" + urlencode({"id": obj.id}))
            html += f'<li><b><a href="{link}" target="_blank">{obj.name}</a></b></li>'
        html += "</ul>"
        return format_html(html)


    list_display = ['name', 'discription']
    list_filter = [field.name for field in models.CourseCategory._meta.fields]
    readonly_fields = ('images',)

    images.short_description = 'images'
    list_display.append("images")

    recent_courses.short_description = 'recent_courses'
    list_display.append("recent_courses")






@admin.register(models.CourseInstructure)
class CourseInstructureAdmin(admin.ModelAdmin):

    class CourseInstructureInline(admin.StackedInline):
        model = models.InstructureImage
        extra = 0

    class CourseInline(admin.TabularInline):
        model = models.Course
        extra = 0

    inlines = [
            CourseInstructureInline,
            CourseInline
            ]

    def images(self, objs):
        html = '<a href="{url}" target="_blank"><img src="{url}" style="width: auto;height: 50px;" /></a>'
        return format_html(''.join(html.format(url=obj.image.url) for obj in objs.course_instructure_image.all()))

    def trainer(self, obj):
        link = (
        reverse("admin:auth_user_changelist")  + "?" + urlencode({"id": obj.user.id})
        )
        return format_html('<b><a href="{}">{}</a></b>', link, obj.user.username)

    def recent_courses(self, objs):
        instances = objs.course_instructure.all()
        if len(instances) >= 5:
            instances = instances[-5]
        html = "<ul>"
        for obj in instances:
            link = (reverse("admin:courses_course_changelist")  + "?" + urlencode({"id": obj.id}))
            html += f'<li><b><a href="{link}" target="_blank">{obj.name}</a></b></li>'
        html += "</ul>"
        return format_html(html)

    trainer.short_description = "Trainer"

    list_display = ["id", 'trainer','discription','job_title','facebook_link','linkedin_link','instagram_link','twitter_link',]
    list_filter = [field.name for field in models.CourseInstructure._meta.fields]
    readonly_fields = ('images',)

    images.short_description = 'images'
    list_display.append("images")

    recent_courses.short_description = 'recent_courses'
    list_display.append("recent_courses")





@admin.register(models.Course)
class CoursesAdmin(admin.ModelAdmin):

    class CourseImagesInline(admin.StackedInline):
        model = models.CourseImage
        extra = 0

    class CourseCommentsInline(admin.StackedInline):
        model = models.CourseComments
        extra = 0

    # class CourseInstructureInline(admin.StackedInline):
    #     model = models.CourseInstructure
    #     extra = 0


    inlines = [
            CourseImagesInline,
            CourseCommentsInline,
            ]

    list_filter = [field.name for field in models.Course._meta.fields]
    readonly_fields = ('images', "comments")
    search_fields = ["name"]

    def images(self, obj):
        html = '<a href="{url}" target="_blank"><img src="{url}" style="width: auto;height: 50px;" /></a>'
        return format_html(''.join(html.format(url=inst.image.url) for inst in obj.course_image.all()))

    def comments(self, obj):
        html = '<a href="{}"<span/>{} | <b>{}</b></span></a>'
        return format_html(''.join(html.format(reverse('admin:comments_comment_change', args=(inst.id,)), inst.comment, inst.name) for inst in obj.course_comment.all()))

    def catagoery(self, obj):
        link = (
        reverse("admin:courses_coursecategory_changelist")  + "?" + urlencode({"id": obj.course_catagoery.id})
        )
        return format_html('<b><a href="{}">{}</a></b>', link, obj.course_catagoery.name)
        # return obj.course_catagoery.id

    catagoery.short_description = "Course Catagoery"

    list_display = ['name', "catagoery", 'course_code', 'course_mode', 'discription']
    list_display.extend(["images","comments"])
    list_display_links = ['name']





