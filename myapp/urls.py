"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.home import views as home_views
from myapp.item import views as item_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', home_views.index),
    # path('products/', item_views.ItemViewSet),
    # path('ingredients/', item_views.ingredient_list),
    # path('ingredients/<int:pk>/', item_views.ingredient_detail),
    path('products/', item_views.products_list),
    path('product/<int:id>', item_views.product_detail),
]
