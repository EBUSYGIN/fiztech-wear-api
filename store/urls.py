from django.urls import path

from . import views


app_name = "store"

urlpatterns = [
    path('api/', views.ProductListView.as_view(), name="store_home"), #Admin path
    path("api/category/", views.CategoryListView.as_view(), name="categories"),
    path("api/<slug:slug>/", views.Product.as_view(), name="product"), #Products under one category (below category) and children elements (use slug like "boots-4")
    path('api/category/<slug:slug>/', views.CategoryItemView.as_view(), name="category_item"), #Individual product
     #Categories path (shoes, boots etc.)
]