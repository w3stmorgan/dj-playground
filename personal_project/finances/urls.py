from django.urls import path

from .views import (
    income_create,
    income_delete,
    income_detail,
    income_list,
    income_update,
)

app_name = "finances"

urlpatterns = [
    path("income-list/", income_list, name="income_list"),
    path("income-create/", income_create, name="income_create"),
    path("income-detail/<pk>", income_detail, name="income_detail"),
    path("income-update/<pk>", income_update, name="income_update"),
    path("income-delete/<pk>", income_delete, name="income_delete"),
]
