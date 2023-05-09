import json
import requests
from datetime import datetime

class IndicatorEconomicAPI:

    BASE_URL = 'https://mindicador.cl/api/'
    MINIMUN_DATE_UF = datetime.strptime("01-01-2013", "%d-%m-%Y")

    @classmethod
    def getIndicator(cls, indicator, date):
        formatDate = date.strftime("%d-%m-%Y")
        url = f'{cls.BASE_URL}{indicator}/{formatDate}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        return data
    
    @classmethod
    def getUf(cls, date):
        if date < cls.MINIMUN_DATE_UF:
            json_response = {
                'accion': 'error',
                'message': 'La fecha ingresada debe ser mayor a 01-01-2013'
            }
            return json_response
        try:
            uf = cls.getIndicator("uf", date)
        except Exception as e:
            json_response = {
                'accion': 'error',
                'message': f'Ocurrió un error al obtener los indicadores económicos: {str(e)}'
            }
            return json_response

        _date = uf['serie'][0]['fecha']
        _value = uf['serie'][0]['valor']

        json_response = {
            'date': _date,
            'value': _value,
            'accion': 'success',
        }
        return json_response