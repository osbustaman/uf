from flask import Flask, jsonify
from datetime import datetime

from utils import indicadores_economicos
app = Flask(__name__)

# Esta línea define una ruta a la que se puede acceder mediante la URL "/get-uf/<day>/<month>/<year>". 
# El método GET indica que solo se puede obtener información a través de esta ruta.
@app.route("/get-uf/<day>/<month>/<year>", methods=['GET'])
def get_uf(day, month, year):

    # En este bloque try-except, se convierte la cadena de fecha (day, month, year) en un objeto datetime de Python.
    # Si la fecha no es válida, se devuelve un mensaje de error.
    try:
        fecha = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")
        fecha_minima = datetime.strptime("01-01-2013", "%d-%m-%Y")
    except ValueError:
        response = {
            'accion': 'error',
            'mensaje': 'La fecha ingresada no es válida'
        }
        return jsonify(response)
    
    # Si la fecha es menor que la fecha mínima establecida (01-01-2013), se devuelve un mensaje de error.
    if fecha < fecha_minima:
        response = {
            'accion': 'error',
            'mensaje': 'La fecha ingresada debe ser mayor a 01-01-2013'
        }
    # De lo contrario, se intenta obtener el valor de la UF para la fecha dada.
    else:
        try:
            uf = indicadores_economicos("uf", fecha)
        except Exception as e:
            # Si ocurre un error al obtener el valor de la UF, se devuelve un mensaje de error con una descripción detallada del error.
            response = {
                'accion': 'error',
                'mensaje': f"Ocurrió un error al obtener los indicadores económicos: {str(e)}"
            }
            return jsonify(response)

        # Si se obtiene con éxito el valor de la UF, se obtiene la fecha y el valor actual de la UF y se devuelve en una respuesta JSON.
        fecha_actual = uf['serie'][0]['fecha']
        valor_actual = uf['serie'][0]['valor']

        response = {
            'fecha': fecha_actual,
            'valor_actual': valor_actual
        }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)