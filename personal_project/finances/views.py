from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import IncomeForm
from .models import Income


class IncomeListView(ListView):
    model = Income
    paginate_by = 50


class IncomeDetailView(DetailView):
    model = Income


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm

    def get_success_url(self) -> str:
        messages.success(self.request, "Income created successfully!")
        return reverse_lazy("finances:income_list")


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm

    def get_success_url(self) -> str:
        messages.success(self.request, "Income updated successfully!")
        return reverse("finances:income_detail", kwargs={"pk": self.object.pk})


class IncomeDeleteView(DeleteView):
    model = Income

    def get_success_url(self) -> str:
        messages.success(self.request, "Income created successfully!")
        return reverse_lazy("finances:income_list")


income_list = IncomeListView.as_view()
income_create = IncomeCreateView.as_view()
income_detail = IncomeDetailView.as_view()
income_update = IncomeUpdateView.as_view()
income_delete = IncomeDeleteView.as_view()
