from flask import Flask, jsonify
from datetime import datetime

from app.api.IndicatorEconomicAPI import IndicatorEconomicAPI

app = Flask(__name__)

def create_app():
    
    # Esta línea define una ruta a la que se puede acceder mediante la URL "/get-uf/<day>/<month>/<year>". 
    # El método GET indica que solo se puede obtener información a través de esta ruta.
    @app.route("/get-uf/<day>/<month>/<year>", methods=['GET'])
    def getUf(day, month, year):
        try:
            fecha = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")
            uf = IndicatorEconomicAPI.getUf(fecha)

            response = {
                'date': uf['date'],
                'value': uf['value'],
                'accion': 'success',
            }
            return jsonify(response)
        except ValueError:
            response = {
                'accion': 'error',
                'message': 'La fecha ingresada no es válida'
            }
            return jsonify(response)
        except Exception as e:
            response = {
                'accion': 'error',
                'message': f'Ocurrió un error al obtener los indicadores económicos: {str(e)}'
            }
            return jsonify(response)

    return app