from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.student_form,name="student_insert"),#insert
    path('<int:id>/',views.student_form,name="student_update"),#update
    path('list/',views.student_list,name="student_list"), #view   
    path('delete/<int:id>/',views.student_delete,name="student_delete"),
]
