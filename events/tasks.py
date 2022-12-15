
from events.models import Event

from datetime import datetime, timezone



def delete_expired_discounts():
    """
    Deletes all Discounts that are more than a minute old
    """
    now_datetime = datetime.now()
    now_datetime = now_datetime.replace(tzinfo=timezone.utc)


    for event in Event.objects.filter(is_done=False):
        print(event.end_date)
        if now_datetime > datetime.combine(event.end_date, event.end_time, tzinfo=timezone.utc):
            event.is_done = True
            event.is_upcomming = False
            event.save()
        else:
            event.is_done = False
            event.is_upcomming = True


# python manage.py qcluster