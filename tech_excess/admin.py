from django.contrib import admin
from .models import Monitors, KeyBoard, Mouse, HeadPhone
# Register your models here.

admin.site.register(Monitors)
admin.site.register(KeyBoard)
admin.site.register(Mouse)
admin.site.register(HeadPhone)