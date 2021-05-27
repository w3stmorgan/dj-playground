class XLSHEADERS():
    COUNTRY = 'country'
    CITY = 'city'
    STATION_NAME = 'stationname'
    AIR_POLLUTANT = 'airpollutant'
    AIR_POLLUTANT_LEVEL = 'airpollutantlevel'
    TYPE = 'type'
    AREA = 'area'
    LONGITUDE = 'longitude'
    LATITUDE = 'latitude'
    ALTITUDE = 'altitude'

    choices = [COUNTRY,CITY,STATION_NAME,AIR_POLLUTANT,AIR_POLLUTANT_LEVEL,TYPE,AREA,LONGITUDE,LATITUDE,ALTITUDE]

def xstr(s) -> str:
    if s is None:
        return ''
    else:
        return s
def get_headers_and_units(ws):
    headers_row = None
    headers = {}
    units = ''

    # Get headers row
    for row in range(ws.max_row +1):
        cell = ws['A'][row].value
        if isinstance(cell, str) and 'country' in cell.lower():
            headers_row = row
            break
    if headers_row is None:
        return None, None, None

    # Remember headers positions
    for i in range(ws.max_column):
        column = chr(i + 65)
        header = xstr(ws[column][headers_row].value)
        header = header.strip().replace('_', '').lower()

        # Get units
        if 'm3' in header:
            units_index = header.find('(') + 1
            for index in range(units_index, units_index+20):
                if header[index] == ')':
                    break
                units += header[index]
            continue
        elif 'unit' in header:
            units = ws[column][headers_row + 1].value
            continue

        # Map headers with their indices
        for choice in XLSHEADERS.choices:
            if choice in header:
                headers[choice] = i

    return headers_row, headers, units
