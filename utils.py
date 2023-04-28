import json
import datetime
import requests

def indicadores_economicos(indicador, fecha_consulta):
    fecha_formateada = fecha_consulta.strftime("%d-%m-%Y")
    url = f'https://mindicador.cl/api/{indicador}/{fecha_formateada}'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data