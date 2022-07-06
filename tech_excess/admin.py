from django.contrib import admin
from .models import Item, ItemReview
# Register your models here.

admin.site.register(Item)
# admin.site.register(KeyBoard)
# admin.site.register(Mouse)
# admin.site.register(HeadPhone)
admin.site.register(ItemReview)