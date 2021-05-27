from django.shortcuts import render
from django import forms
import openpyxl

from ..airpollution.models import Pollutant, Country
from ..airpollution.helpers import get_headers_and_units

class ExcelUploadForm(forms.Form):
    year = forms.CharField(max_length=4)
    file = forms.FileField()

def welcome(request):
    context = {
        'app_name': request.resolver_match.app_name
    }
    return render(request, 'airpollution/welcome.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            wb = openpyxl.load_workbook(filename=file, read_only=False)
            tab_names = wb.get_sheet_names()
            for tab_name in tab_names:
                ws = wb[tab_name]
                pollutant_name = tab_name.split('_')[0]
                pollutant = Pollutant.objects.get_or_create(name=pollutant_name)
                headers_row, header, units = get_headers_and_units(ws)
                print('test∂')
    else:
        pass
    context = {
        'app_name': request.resolver_match.app_name,
        'message_success': 'File uploaded successfully!'
    }
    return render(request, 'airpollution/welcome.html', context)


def temp_country_creator(request):
    countries = {
        'Montenegro': 'ME',
        'Andorra': 'AD',
        'Albania': 'AL',
        'Austria': 'AT',
        'Bosnia and Herzegovina': 'BA',
        'Belgium': 'BE',
        'Bulgaria': 'BG',
        'Switzerland': 'CH',
        'Serbia': 'CS',
        'Cyprus': 'CY',
        'Czech Republic': 'CZ',
        'Germany': 'DE',
        'Denmark': 'DK',
        'Estonia': 'EE',
        'Spain': 'ES',
        'Finland': 'FI',
        'France': 'FR',
        'United Kingdom': 'GB',
        'Greece': 'GR',
        'Croatia': 'HR',
        'Hungary': 'HU',
        'Ireland': 'IE',
        'Iceland': 'IS',
        'Italy': 'IT',
        'Lithuania': 'LT',
        'Luxembourg': 'LU',
        'Latvia': 'LV',
        'The former Yugoslav Republic of Macedonia': 'MK',
        'Malta': 'MT',
        'Netherlands': 'NL',
        'Norway': 'NO',
        'Poland': 'PL',
        'Portugal': 'PT',
        'Romania': 'RO',
        'Sweden': 'SE',
        'Slovenia': 'SI',
        'Slovakia': 'SK',
        'Turkey': 'TR',
        'Kosovo under UNSCR 1244/99': 'XK',
    }

    to_insert = []
    for country_name, iso_code in countries.items():
        to_insert.append(Country(iso_code=iso_code, name=country_name))
    Country.objects.bulk_create(to_insert)

    context = {
        'app_name': request.resolver_match.app_name,
        'message_success': 'Countries created!'
    }
    return render(request, 'airpollution/welcome.html', context)
