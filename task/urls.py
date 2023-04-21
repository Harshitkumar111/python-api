from django.urls import path
from . import views


urlpatterns = [
    path("", views.index , name="index"),
    path("save", views.save , name="save"),
    path("update/<int:id>", views.update , name="update"),
    path("delete/<int:id>", views.destroy , name="delete"),
    path("dataapi/<int:id>", views.api,name="dataapi"),
     
]