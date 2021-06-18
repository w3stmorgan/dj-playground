from django.urls import path

from .views import (
    income_create,
    income_delete,
    income_detail,
    income_list,
    income_update,
    outcome_create,
    outcome_delete,
    outcome_detail,
    outcome_list,
    outcome_update,
)

app_name = "finances"

urlpatterns = [
    path("outcome-list/", outcome_list, name="outcome_list"),
    path("outcome-create/", outcome_create, name="outcome_create"),
    path("outcome-detail/<pk>", outcome_detail, name="outcome_detail"),
    path("outcome-update/<pk>", outcome_update, name="outcome_update"),
    path("outcome-delete/<pk>", outcome_delete, name="outcome_delete"),
    path("income-list/", income_list, name="income_list"),
    path("income-create/", income_create, name="income_create"),
    path("income-detail/<pk>", income_detail, name="income_detail"),
    path("income-update/<pk>", income_update, name="income_update"),
    path("income-delete/<pk>", income_delete, name="income_delete"),
]
