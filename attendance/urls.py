from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('unit/<int:unit_id>', views.unit),
    path('unit/<int:unit_id>/new/', views.new),
    path('view/<int:attendance_id>', views.view),
]
