from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms
from events.models import Event
from datetime import datetime

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields='__all__'
        # fields.extend(["created_at", "updated_at",])
        exclude = ["id", "created_at", "updated_at",]
        widgets = {
            "start_date": DatePickerInput(),
            "start_time": TimePickerInput(),
            "end_date": DatePickerInput(),
            "end_time": TimePickerInput()
        }