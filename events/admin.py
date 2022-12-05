from django.contrib import admin
import events.models as models


@admin.register(models.EventImage)
class EventImage(admin.ModelAdmin):
    pass
@admin.register(models.EventComment)
class EventComment(admin.ModelAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Event._meta.fields]
    list_filter = list_display

@admin.register(models.EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.EventType._meta.fields]
    list_filter = list_display

@admin.register(models.EventSchedule)
class EventScheduleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.EventSchedule._meta.fields]
    list_filter = list_display
