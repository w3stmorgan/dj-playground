from django.contrib import admin

from .models import Balance, Income, Outcome

admin.site.register(Income)
admin.site.register(Outcome)
admin.site.register(Balance)
