from django.urls import path
from .views import AddOrRemoveStars, AddToBasket, AllItemCommentsView, CategoryListView, CreateComment, DeleteCommentView, ItemDetailView, ShopPageView, ajax_results,ResultSearchView

urlpatterns = [
    path('',ShopPageView.as_view(),name="home2"),
    path('add/<pk>/<int:num>',AddToBasket.as_view(),name='add'),
    path('search-results/',ResultSearchView.as_view(),name='results'),
    path('search-results/search/',ajax_results,name='serchng'),
    path('category/<pk>/',CategoryListView.as_view(),name='catlist'),
    path('item-detail/<pk>/view/',ItemDetailView.as_view(),name='item'),
    path('<pk>/addcomment/',CreateComment.as_view(),name='comment'),
    path('<pk>/setstars/',AddOrRemoveStars.as_view(),name='stars_set'),
    path('<pk>/deletecom/<pk2>',DeleteCommentView.as_view(),name='deletecom'),
    path('item/<pk>/comments/',AllItemCommentsView.as_view(),name='coms')
    ]