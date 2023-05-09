from flask import Flask, jsonify
from datetime import datetime

from app.api.IndicadorEconomicoAPI import IndicadorEconomicoAPI

def create_app():
    app = Flask(__name__)

    # Esta línea define una ruta a la que se puede acceder mediante la URL "/get-uf/<day>/<month>/<year>". 
    # El método GET indica que solo se puede obtener información a través de esta ruta.
    @app.route("/get-uf/<day>/<month>/<year>", methods=['GET'])
    def get_uf(day, month, year):

        try:
            fecha = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")
            ie = IndicadorEconomicoAPI()
            uf = ie.get_uf(fecha)

            response = {
                'fecha': uf['fecha'],
                'valor_actual': uf['valor_actual']
            }
            return jsonify(response)
        except ValueError:
            response = {
                'accion': 'error',
                'mensaje': 'La fecha ingresada no es válida'
            }
            return jsonify(response)
        except Exception as e:
            response = {
                'accion': 'error',
                'mensaje': f'Ocurrió un error al obtener los indicadores económicos: {str(e)}'
            }
            return jsonify(response)

    return app