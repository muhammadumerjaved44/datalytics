from django.contrib import admin
import events.models as models
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# @admin.register(models.EventImage)
# class EventImage(admin.ModelAdmin):
#     pass
# @admin.register(models.EventComment)
# class EventComment(admin.ModelAdmin):
#     pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    class EventsImageInline(admin.StackedInline):
        model = models.EventImage
        extra = 0

    class EventCommentInline(admin.StackedInline):
        model = models.EventComment
        extra = 0

    inlines = [
        EventsImageInline,
        EventCommentInline
            ]

    def images(self, objs):
        html = '<a href="{url}" target="_blank"><img src="{url}" style="width: auto;height: 50px;" /></a>'
        html = '<img src="{url}" style="width: auto;height: 50px;" />'
        return format_html(''.join(html.format(url=obj.image.url) for obj in objs.event_images.all()))

    def comments(self, obj):
        html = '<a href="{}"<span/>{} | <b>{}</b></span></a>'
        return format_html(''.join(html.format(reverse('admin:comments_comment_change', args=(inst.id,)), inst.comment, inst.name) for inst in obj.event_comments.all()))


    list_display = [field.name for field in models.Event._meta.fields]
    list_filter = [field.name for field in models.Event._meta.fields]
    readonly_fields = ('images', "comments")

    # images.short_description = 'images'
    list_display.append("images")
    list_display.append("comments")


@admin.register(models.EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.EventType._meta.fields]
    list_filter = list_display

