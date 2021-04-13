from django.urls import path
from employee_app import views

urlpatterns = [
    path("",views.ListEmployeeAPIView.as_view(),name="employee_list"),
    path("create/", views.CreateEmployeeAPIView.as_view(),name="employee_create"),
    path("update/<int:pk>/",views.UpdateEmployeeAPIView.as_view(),name="update_employee"),
    path("delete/<int:pk>/",views.DeleteEmployeeAPIView.as_view(),name="delete_employee")
]