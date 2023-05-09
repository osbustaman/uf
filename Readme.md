## PASO 1: Instalar python, en el caso de ya tenerlo omitir el paso 1
## PASO 2: crear entorno virtual con virtualenv
## PASO 3: instalar requirements.txt en el entorno virtual
## PASO 4: ejecutar

## Desafío: Creación de API para consultar la Unidad de Fomento en Python

### El Servicio de Impuestos Internos (SII) de Chile mantiene una tabla con los valores de la Unidad de Fomento actualizados para cada año. Tu desafío consiste en crear una API en Python que permita a los usuarios consultar el valor de la Unidad de Fomento para una fecha específica.


![Screenshot 2023-04-17 111742](https://user-images.githubusercontent.com/3030497/232532665-86703af1-3e7e-4147-9fe1-89cd35889334.png)

### Requisitos:

- La API debe estar desarrollada en Python utilizando la librería "requests" u otra similar.
- No se puede utilizar Selenium debido al alto consumo de recursos que estas herramientas implican.
- La API debe permitir consultar el valor de la Unidad de Fomento para una fecha específica, la cual debe ser ingresada como parámetro en la solicitud.
- La fecha mínima que se puede consultar es el 01-01-2013, y no hay fecha máxima, ya que la tabla se actualiza constantemente.
- La API debe devolver el valor de la Unidad de Fomento correspondiente a la fecha consultada.
- La respuesta de la API debe estar en formato JSON.


Para ayudarte en el desarrollo de este desafío, puedes utilizar la tabla de valores de la Unidad de Fomento actualizados para cada año que se encuentra en el siguiente enlace: https://www.sii.cl/valores_y_fechas/uf/uf2023.htm

### Que validaremos:
#### Nos importa la creatividad a la hora del desarrollo y la calidad de codigo, por eso validaremos los siguentes puntos:
- Que sea un codigo limpio
- Que sea un codigo dinamico
- Manejo de Errores

### importante, pero no necesario:
- Utilizar SOLID
- Tener Testing

### Entregable
#### Es necesario enviar un repositorio de git con el desafio a desafio_ti@fapro.app


¡Buena suerte!
