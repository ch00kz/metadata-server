from django.utils import timezone
from datetime import timedelta

def get_current_datetime():
	return timezone.now()

def get_refresh_datetime():
	return timezone.now() + timedelta(days=1)
