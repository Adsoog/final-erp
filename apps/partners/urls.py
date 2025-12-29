from django.urls import path
from .views import partners

urlpatterns = [
    path("list/", partners.partner_list, name="partner_list"),
    path("create/", partners.partner_create, name="partner_create")
]
