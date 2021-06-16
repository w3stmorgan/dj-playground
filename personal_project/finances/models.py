from django.db import models


class Income(models.Model):
    class ITypes(models.IntegerChoices):
        SAL = 1, "SALARY"
        BON = 2, "BONUS"
        GIF = 3, "GIFT"
        OTH = 4, "OTHER"

    class RInterval(models.IntegerChoices):
        DAY = 1, "DAYS"
        WEE = 2, "WEEKS"
        MON = 3, "MONTHS"
        YEA = 4, "YEARS"
        NA = 5, "N/A"

    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=ITypes.choices)
    repetitive = models.BooleanField(default=False)
    repetitive_interval = models.PositiveSmallIntegerField(
        choices=RInterval.choices, default=5
    )
    repetitive_time = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Income {self.id} - {self.type} {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = "incomes"


class Outcome(models.Model):
    class OTypes(models.IntegerChoices):
        REN = 1, "RENT"
        BIL = 2, "BILLS"
        CAR = 3, "CAR"
        TRA = 4, "TRAVEL"
        HEA = 5, "HEALTH"
        GRO = 6, "GROCERIES"
        FUN = 7, "FUN"
        CLO = 8, "CLOTHES"
        CHA = 9, "CHARITY"

    class RInterval(models.IntegerChoices):
        DAY = 1, "DAYS"
        WEE = 2, "WEEKS"
        MON = 3, "MONTHS"
        YEA = 4, "YEARS"
        NA = 5, "N/A"

    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=OTypes.choices)
    repetitive = models.BooleanField(default=False)
    repetitive_interval = models.PositiveSmallIntegerField(
        choices=RInterval.choices, default=5
    )
    repetitive_time = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Outcome {self.id} - {self.type} {self.date.strftime("%Y/%m/%d")}'

    class Meta:
        verbose_name_plural = "outcomes"


class Balance(models.Model):
    class BTypes(models.IntegerChoices):
        CUR = 1, "CURRENT"
        SAV = 2, "SAVINGS"

    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.PositiveSmallIntegerField(choices=BTypes.choices)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Income {self.id} - {self.type} {self.updated_at.strftime("%Y/%m/%d %H:%M:%S")}'

    class Meta:
        verbose_name_plural = "balances"
