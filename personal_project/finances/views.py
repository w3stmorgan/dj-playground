from django.contrib import messages
from django.db.models import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import IncomeForm, OutcomeForm
from .models import Income, Outcome


class IncomeListView(ListView):
    model = Income
    paginate_by = 50
    template_name = "finances/income_outcome_list.html"
    extra_context = {"type": "Income"}

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Income.objects.filter(user=user)


class IncomeDetailView(DetailView):
    model = Income
    template_name = "finances/income_outcome_detail.html"
    extra_context = {"type": "Income"}

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Income.objects.filter(user=user)


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = "finances/income_outcome_form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        messages.success(self.request, "Income created successfully!")
        return reverse_lazy("finances:income_list")


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = "finances/income_outcome_form.html"

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Income.objects.filter(user=user)

    def get_success_url(self) -> str:
        messages.success(self.request, "Income updated successfully!")
        return reverse("finances:income_detail", kwargs={"pk": self.object.pk})


class IncomeDeleteView(DeleteView):
    model = Income
    template_name = "finances/income_outcome_confirm_delete.html"

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Income.objects.filter(user=user)

    def get_success_url(self) -> str:
        messages.success(self.request, "Income deleted successfully!")
        return reverse_lazy("finances:income_list")


class OutcomeListView(ListView):
    model = Outcome
    paginate_by = 50
    template_name = "finances/income_outcome_list.html"
    extra_context = {"type": "Outcome"}

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Outcome.objects.filter(user=user)


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = "finances/income_outcome_detail.html"
    extra_context = {"type": "Outcome"}

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Outcome.objects.filter(user=user)


class OutcomeCreateView(CreateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = "finances/income_outcome_form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        messages.success(self.request, "Outcome created successfully!")
        return reverse_lazy("finances:outcome_list")


class OutcomeUpdateView(UpdateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = "finances/income_outcome_form.html"

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self) -> str:
        messages.success(self.request, "Outcome updated successfully!")
        return reverse("finances:outcome_detail", kwargs={"pk": self.object.pk})


class OutcomeDeleteView(DeleteView):
    model = Outcome
    template_name = "finances/income_outcome_confirm_delete.html"

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self) -> str:
        messages.success(self.request, "Outcome deleted successfully!")
        return reverse_lazy("finances:outcome_list")


outcome_list = OutcomeListView.as_view()
outcome_create = OutcomeCreateView.as_view()
outcome_detail = OutcomeDetailView.as_view()
outcome_update = OutcomeUpdateView.as_view()
outcome_delete = OutcomeDeleteView.as_view()

income_list = IncomeListView.as_view()
income_create = IncomeCreateView.as_view()
income_detail = IncomeDetailView.as_view()
income_update = IncomeUpdateView.as_view()
income_delete = IncomeDeleteView.as_view()
