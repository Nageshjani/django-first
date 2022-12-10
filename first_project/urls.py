
from django.contrib import admin
from django.urls import path,include
from app1 import views
from employee.views import show
from employee.views import emp
from employee.views import edit
from employee.views import update

from employee.views import destroy
from email_reg.views import signup_form


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('image/',views.image),
    path('css/',views.css),
    path('show/',show),
    path('emp/',emp),
    path('edit/<int:id>/',edit),
    path('update/<int:id>/',update),

    path('delete/<int:id>/',destroy),
    path('signup/',signup_form),


]
