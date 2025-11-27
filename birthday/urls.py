from django.urls import path
from .views import birthday_create, birthday_list

urlpatterns = [
    path("aniversarios/", birthday_list, name="birthday_list"),
    path("aniversarios/novo/", birthday_create, name="birthday_create"),
]
