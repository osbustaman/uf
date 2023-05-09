from flask import Flask, jsonify
from datetime import datetime
from app.api.IndicatorEconomicAPI import IndicatorEconomicAPI

# Se crea una nueva aplicación Flask
app = Flask(__name__)

# Se define una función para crear la aplicación
def create_app():

    # Se define una ruta a la que se puede acceder mediante la URL "/get-uf/<day>/<month>/<year>" y utilizando el método GET.
    # Esta ruta es utilizada para obtener la UF (Unidad de Fomento) para una fecha específica.
    @app.route("/get-uf/<day>/<month>/<year>", methods=['GET'])
    def getUf(day, month, year):
        try:
            # Se intenta convertir la fecha ingresada por el usuario en un objeto datetime.
            fecha = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")

            # Se llama a la función getUf de la clase IndicatorEconomicAPI, que devuelve el valor de la UF para una fecha determinada.
            uf = IndicatorEconomicAPI.getUf(fecha)

            # Se crea un diccionario con los valores de la fecha y el valor de la UF, y se devuelve como una respuesta JSON.
            response = {
                'date': uf['date'],
                'value': uf['value'],
                'accion': 'success',
            }
            return jsonify(response), 200

        # Si la fecha ingresada no es válida, se devuelve un mensaje de error.
        except ValueError:
            response = {
                'accion': 'error',
                'message': 'La fecha ingresada no es válida'
            }
            return jsonify(response), 404

        # Si ocurre algún otro tipo de error, se devuelve un mensaje de error genérico.
        except Exception as e:
            response = {
                'accion': 'error',
                'message': f'Ocurrió un error al obtener los indicadores económicos: {str(e)}'
            }
            return jsonify(response), 404

    return app
