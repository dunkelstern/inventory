"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path

from .views import (
    WorkshopListView,
    AreaListView,
    BoxListView,
    ItemListView,
    ManufacturerListView,
    DistributorListView,
    TagListView
)
from .views import (
    WorkshopView,
    AreaView,
    BoxView,
    ItemView,
    DistributorView,
    ManufacturerView,
    IndexView,
    TagView
)

urlpatterns = [
    path('workshops', WorkshopListView.as_view(), name='workshop-list'),
    path('workshop/<int:pk>/areas', AreaListView.as_view(), name='area-list'),
    path('workshop/<int:pk>', WorkshopView.as_view(), name='workshop-detail'),
    path('area/<int:pk>/boxes', BoxListView.as_view(), name='box-list'),
    path('area/<int:pk>', AreaView.as_view(), name='area-detail'),
    path('box/<int:pk>/items', ItemListView.as_view(), name='item-list'),
    path('box/<int:pk>/boxes', BoxListView.as_view(), name='box-recurse-list'),
    path('box/<int:pk>', BoxView.as_view(), name='box-detail'),
    path('item/<int:pk>', ItemView.as_view(), name='item-detail'),
    path('manufacturers', ManufacturerListView.as_view(), name='manufacturer-list'),
    path('manufacturer/<int:pk>', ManufacturerView.as_view(), name='manufacturer-detail'),
    path('distributors', DistributorListView.as_view(), name='distributor-list'),
    path('distributor/<int:pk>', DistributorView.as_view(), name='distributor-detail'),
    path('tags', TagListView.as_view(), name='tag-list'),
    path('tag/<int:pk>', TagView.as_view(), name='tag-detail'),
    path('', IndexView.as_view(), name='index')
]
