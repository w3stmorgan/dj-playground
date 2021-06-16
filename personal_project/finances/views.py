from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Income


class IncomeListView(ListView):
    model = Income
    paginate_by = 50


class IncomeDetailView(DetailView):
    model = Income


class IncomeCreateView(CreateView):
    model = Income
    fields = [
        "value",
        "date",
        "type",
        "repetitive",
        "repetitive_interval",
        "repetitive_time",
    ]
    success_url = reverse_lazy("finances:income_list")


class IncomeUpdateView(UpdateView):
    model = Income
    fields = [
        "value",
        "date",
        "type",
        "repetitive",
        "repetitive_interval",
        "repetitive_time",
    ]
    success_url = reverse_lazy("finances:income_list")


class IncomeDeleteView(DeleteView):
    model = Income
    success_url = reverse_lazy("finances:income_list")


income_list = IncomeListView.as_view()
income_create = IncomeCreateView.as_view()
income_detail = IncomeDetailView.as_view()
income_update = IncomeUpdateView.as_view()
income_delete = IncomeDeleteView.as_view()
