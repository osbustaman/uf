import json
import requests
from datetime import datetime

class IndicadorEconomicoAPI:
    def __init__(self) -> None:
        self.base_url = 'https://mindicador.cl/api/'
        self.fecha_minima_uf = datetime.strptime("01-01-2013", "%d-%m-%Y")

    def get_indicador(self, indicador, fecha_consulta):
        fecha_formateada = fecha_consulta.strftime("%d-%m-%Y")
        url = f'{self.base_url}{indicador}/{fecha_formateada}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        return data
    
    def get_uf(self, fecha):
        if fecha < self.fecha_minima_uf:
            json_response = {
                'accion': 'error',
                'mensaje': 'La fecha ingresada debe ser mayor a 01-01-2013'
            }
            return json_response
        try:
            uf = self.get_indicador("uf", fecha)
        except Exception as e:
            json_response = {
                'accion': 'error',
                'mensaje': f'Ocurrió un error al obtener los indicadores económicos: {str(e)}'
            }
            return json_response

        fecha_actual = uf['serie'][0]['fecha']
        valor_actual = uf['serie'][0]['valor']

        json_response = {
            'fecha': fecha_actual,
            'valor_actual': valor_actual
        }
        return json_response