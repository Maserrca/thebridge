from flask import Flask, request, render_template
from utils.functions import read_json
import os

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  --> OBLIGATORIO

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función, LA BARRITA ES EL SEPARADOR POR DEFECTO
def home():
    """ Default path """
    return app.send_static_file('greet.html')

@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/info")
def create_json():
    return 'Tienes que acceder al endpoint "/give_me_id" pasando por parámetro "password" con la contraseña correcta' 

@app.route('/give_me_id', methods=['GET'])
def give_id():
    x = request.args['password']
    if x == "12345":
        return request.args
    else:
        return "No es la contraseña correcta"
##Para meter todo eso en la ruta se añade el parametro give me id  y para darle el siguente parametro se usa interogacion 
# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    # Para ambos: os.sep
    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file)  
    ##Esta funcion esta leyendo el json del archivo settings mas abajo para pasarlo a un diccionariio, para comprobarlo ir al archivo de funciones
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    print("SERVER_RUNNING", SERVER_RUNNING)
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
            "Please, allow it to run it.")

if __name__ == "__main__":
    main()