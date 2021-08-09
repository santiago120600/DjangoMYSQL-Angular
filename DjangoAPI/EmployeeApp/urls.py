from django.conf.urls import url
from EmployeeApp import views 

urlpatterns = [
    url(r'^department$',views.departamentApi),
    url(r'^department/([0-9]+)$',views.departamentApi)
]
