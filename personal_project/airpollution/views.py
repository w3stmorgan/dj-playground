from django.http import HttpResponse
from django.db.models import Q, Sum, Count
from django.shortcuts import render
from django import forms
import openpyxl
import colorsys
import json

from ..airpollution.models import Pollutant, Country, PollutantEntry
from ..airpollution.helpers import get_headers_and_units, XLSHEADERS

class ExcelUploadForm(forms.Form):
    year = forms.CharField(max_length=4)
    file = forms.FileField()


def airpollution(request):
    if request.method == 'GET':
        table_data = {}
        visuals_data = {}
        pollutant_list = [pollutant.name for pollutant in Pollutant.objects.all()]
        country_list = [country.iso_code for country in Country.objects.all()]

        for pollutant in pollutant_list:
            table_data[pollutant] = {}
            visuals_data[pollutant] = {'labels': [], 'data': []}
            for country in country_list:
                total = PollutantEntry.objects\
                    .aggregate(total=Sum('pollution_level', filter=Q(pollutant__name=pollutant,
                                                                     country__iso_code=country)))
                total = total['total']
                count = PollutantEntry.objects.filter(pollutant__name=pollutant, country__iso_code=country).count()
                if total is not None and count:
                    table_data[pollutant][country] = total / count
                    visuals_data[pollutant]['labels'].append(country)
                    visuals_data[pollutant]['data'].append(total / count)

        for pollutant_data in visuals_data.values():
            data_count = len(pollutant_data['labels'])
            HSV_tuples = [(i * 1.0 / data_count, 0.5, 0.5) for i in range(data_count)]
            RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
            background_colors = []
            border_colors = []
            for rgb in RGB_tuples:
                red, green, blue = int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)
                background_colors.append(f'rgba({red}, {green}, {blue}, 0.2)')
                border_colors.append(f'rgba({red}, {green}, {blue}, 1)')

            pollutant_data['labels'] = json.dumps(pollutant_data['labels'])
            pollutant_data['data'] = json.dumps(pollutant_data['data'])
            pollutant_data['background'] = json.dumps(background_colors)
            pollutant_data['border'] = json.dumps(border_colors)

        context = {
            'app_name': request.resolver_match.app_name,
            'data': table_data,
            'visuals_data': visuals_data,
        }
    elif request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            year = form.cleaned_data['year']
            file = form.cleaned_data['file']
            wb = openpyxl.load_workbook(filename=file, read_only=False)
            tab_names = wb.get_sheet_names()
            for tab_name in tab_names:
                ws = wb[tab_name]
                pollutant_name = tab_name.split('_')[0].strip()
                pollutant = Pollutant.objects.get_or_create(name=pollutant_name)
                headers_row, headers, units = get_headers_and_units(ws)

                # Save all entries to database
                to_insert = []
                for i, row in enumerate(ws.rows):
                    if i <= headers_row:  # Skip to actual entries
                        continue

                    country = row[headers[XLSHEADERS.COUNTRY]].value
                    if country is None:
                        break
                    if len(country) > 2:
                        country_object = Country.objects.filter(name=country).first()
                    else:
                        country_object = Country.objects.get(pk=country)

                    city = row[headers[XLSHEADERS.CITY]].value
                    station_name = row[headers[XLSHEADERS.STATION_NAME]].value
                    station_area = row[headers[XLSHEADERS.AREA]].value

                    data = {
                        'pollutant': pollutant[0],
                        'country': country_object,
                        'year': year,
                        'city': city if city else '',
                        'station_code': row[headers[XLSHEADERS.STATION_EOI_CODE]].value,
                        'station_name': station_name if station_name else '',
                        'pollution_level': row[headers[XLSHEADERS.AIR_POLLUTANT_LEVEL]].value,
                        'units': units,
                        'station_type': row[headers[XLSHEADERS.TYPE]].value,
                        'station_area': station_area if station_area else '',
                        'longitude': row[headers[XLSHEADERS.LONGITUDE]].value,
                        'latitude': row[headers[XLSHEADERS.LATITUDE]].value,
                        'altitude': row[headers[XLSHEADERS.ALTITUDE]].value,
                    }
                    to_insert.append(PollutantEntry(**data))

                PollutantEntry.objects.filter(year=year, pollutant=pollutant[0]).delete()
                PollutantEntry.objects.bulk_create(to_insert)
        context = {
            'app_name': request.resolver_match.app_name,
            'message_success': 'File uploaded successfully!'
        }
    else:  # request method not POST
        return HttpResponse("Only accepted methods are GET nad POST!")

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
