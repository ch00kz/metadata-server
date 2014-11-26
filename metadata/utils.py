from django.utils import timezone
from datetime import timedelta

def get_current_time():
    return timezone.localtime(timezone.now())

def get_token_refresh_time():
	return timezone.localtime(timezone.now()) + timedelta(days=1)
