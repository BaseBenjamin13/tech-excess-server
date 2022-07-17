from django.contrib import admin
from .models import Item, ItemReview, Wishlist, Cart
# Register your models here.

admin.site.register(Item)
admin.site.register(ItemReview)
admin.site.register(Wishlist)
admin.site.register(Cart)