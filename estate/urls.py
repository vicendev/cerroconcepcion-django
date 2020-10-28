from django.urls import path
from . import views

urlpatterns = [
    path('', views.estate_list, name="estates"),
    path('create/', views.estate_create, name="estate_create"),
    path('<int:pk>/', views.estate_detail, name='estate-detail'),
    path('update/<int:pk>', views.estate_update, name='estate-update'),
    path('image/delete/', views.delete_image_update, name='images-delete'),
    path('delete/<int:pk>', views.estate_delete, name="estate-delete"),
]