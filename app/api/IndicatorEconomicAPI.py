import json
import requests
from datetime import datetime

# Se define una clase llamada IndicatorEconomicAPI
class IndicatorEconomicAPI:

    # Se define la URL base de la API y la fecha mínima permitida para obtener el valor de la UF.
    BASE_URL = 'https://mindicador.cl/api/'
    MINIMUN_DATE_UF = datetime.strptime("01-01-2013", "%d-%m-%Y")

    # Se define un método estático para obtener los valores de un indicador económico para una fecha determinada.
    @classmethod
    def getIndicator(cls, indicator, date):
        # Se formatea la fecha en el formato correcto para la API.
        formatDate = date.strftime("%d-%m-%Y")
        # Se construye la URL para obtener los valores del indicador económico en la fecha indicada.
        url = f'{cls.BASE_URL}{indicator}/{formatDate}'
        # Se realiza una petición GET a la API para obtener los datos.
        response = requests.get(url)
        # Se convierte la respuesta a un objeto JSON.
        data = json.loads(response.text.encode("utf-8"))
        # Se devuelve el objeto JSON.
        return data
    
    # Se define un método estático para obtener el valor de la UF para una fecha determinada.
    @classmethod
    def getUf(cls, date):
        # Se verifica si la fecha es mayor o igual a la fecha mínima permitida para obtener el valor de la UF.
        if date < cls.MINIMUN_DATE_UF:
            # Si la fecha no es válida, se devuelve un mensaje de error.
            json_response = {
                'accion': 'error',
                'message': ('La fecha ingresada debe ser mayor a 01-01-2013').encode('utf-8')
            }
            return jsonify(json_response), 404

        try:
            # Se llama al método getIndicator para obtener el valor de la UF en la fecha indicada.
            uf = cls.getIndicator("uf", date)
        except Exception as e:
            # Si ocurre un error, se devuelve un mensaje de error.
            json_response = {
                'accion': 'error',
                'message': (f'Ocurrió un error al obtener los indicadores económicos: {str(e)}').encode('utf-8')
            }
            return jsonify(json_response), 404

        # Se extrae la fecha y el valor de la UF del objeto JSON obtenido.
        _date = uf['serie'][0]['fecha']
        _value = uf['serie'][0]['valor']

        # Se crea un diccionario con los valores de la fecha y el valor de la UF, y se devuelve como respuesta.
        json_response = {
            'date': _date,
            'value': _value,
            'accion': 'success',
        }
        return json_response
