from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alba/', views.AlbumListView.as_view(), name='alba'),
    path('alba/<int:pk>', views.AlbumDetailView.as_view(), name='alba_detail')
]