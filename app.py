from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def conectar_bd():
    return psycopg2.connect(
        host="localhost", database="bd_nudelpa",
        user="postgres", password="TU_CONTRASEÑA"
    )

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formulario_completo')
def formulario_completo():
    return render_template('formulario_completo.html')

@app.route('/guardar_todo', methods=['POST'])
def guardar_todo():
    # Recibimos TODO el diccionario de datos del formulario
    datos = request.form
    
    # Ejemplo de cómo capturar uno de los campos específicos:
    dia = datos.get('dia')
    mes = datos.get('mes')
    anio = datos.get('anio')
    num_rep = datos.get('num_reporte')
    
    print(f"Recibido Reporte NUDELPA Nº {num_rep} del {dia}/{mes}/{anio}")
    
    # Aquí puedes añadir el código para guardar cada campo en su tabla de Postgres
    
    return f"<h2>Reporte Nº {num_rep} guardado exitosamente.</h2><br><a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)