from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('unit', views.index),
    path('unit/<int:unit_id>', views.unit),
    path('unit/<int:unit_id>/new/', views.new),
    path('student/<int:student_id>', views.student),
    path('unit/<int:unit_id>/view/', views.attendances),
    path('view/<int:attendance_id>', views.view),
]
