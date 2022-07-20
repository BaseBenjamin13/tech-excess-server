
from django.shortcuts import render

from django.http import JsonResponse
from rest_framework import generics , permissions
from .serializers import ItemsSerializer,  ItemReviewSerializer, WishlistSerializer, CartSerializer
from .models import Item, ItemReview, Wishlist

# Create your views here.

from rest_framework.permissions import AllowAny


#Items
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer


class ItemEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer


class MonitorList(generics.ListCreateAPIView):
    queryset = Item.objects.filter(category='monitor')
    serializer_class = ItemsSerializer

class KeyboardList(generics.ListCreateAPIView):
    queryset = Item.objects.filter(category='keyboard')
    serializer_class = ItemsSerializer

class MouseList(generics.ListCreateAPIView):
    queryset = Item.objects.filter(category='mouse')
    serializer_class = ItemsSerializer

class HeadphoneList(generics.ListCreateAPIView):
    queryset = Item.objects.filter(category='headphone')
    serializer_class = ItemsSerializer


#Reviews
class ItemReviewsList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = ItemReview.objects.all()
    serializer_class = ItemReviewSerializer

#Create review only if logged in.
class CreateReview(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = ItemReview.objects.all()
    serializer_class = ItemReviewSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ItemReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = ItemReview.objects.all()
    serializer_class = ItemReviewSerializer

#delete or edit review
class ItemReviewsChange(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = ItemReview.objects.all()
    serializer_class = ItemReviewSerializer


#wishlists
class WishlistList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = WishlistSerializer
    def get_queryset(self):
        return self.request.user.wishlists.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = WishlistSerializer
    def get_queryset(self):
        return self.request.user.wishlists.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


#CARTS
class CartList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CartSerializer
    def get_queryset(self):
        return self.request.user.carts.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
#cart that is not completed yet:
class CartInProgress(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CartSerializer
    def get_queryset(self):
        return self.request.user.carts.filter(order_completed=False)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

#cart that is completed:
class CartCompleted(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CartSerializer
    def get_queryset(self):
        return self.request.user.carts.filter(order_completed=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CartSerializer
    def get_queryset(self):
        return self.request.user.carts.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



#https://www.youtube.com/watch?v=0d7cIfiydAc
#user tutorial
#display reviews made by a user.
class UsersReviewsList(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    # queryset = ItemReview.objects.all()
    serializer_class = ItemReviewSerializer

    def get_queryset(self):
        return self.request.user.reviews.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

