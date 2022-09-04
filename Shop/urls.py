from django.urls import path
from .views import AddToBasket, CategoryListView, ItemDetailView, ShopPageView, ajax_results,ResultSearchView

urlpatterns = [
    path('',ShopPageView.as_view(),name="home2"),
    path('add/<pk>',AddToBasket.as_view(),name='add'),
    path('search-results/',ResultSearchView.as_view(),name='results'),
    path('search-results/search/',ajax_results,name='serchng'),
    path('category/<pk>/',CategoryListView.as_view(),name='catlist'),
    path('item-detail/<pk>/view',ItemDetailView.as_view(),name='item'),
    ]