from flask import Flask, request, render_template
import requests

app = Flask(__name__)

#app route principal (index.html)
@app.route('/', methods=["GET", "POST"])
def index(): 
    weatherData = None  # Contendrá el json de la información de la temperatura
    error = None #para mostrar mensaje de error
    cityName = '' #para el nombre de la ciudad
    
    if request.method == "POST":       
        cityName = request.form.get("cityName")  
        if cityName:
            weatherApiKey = 'e9e35eb6363871a3e64fe885af360449'  # Clave API a utilizar
            # Se agregó el código del país para una mejor precisión
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName},EC&appid={weatherApiKey}&units=metric"
            weatherData = requests.get(url).json()

            # Se Verifica si hay errores en la respuesta de la API
            if weatherData.get("cod") != 200:  #Si el codigo es distinto a 200 
                error = weatherData.get("message")  # Mensaje de error devuelto por la API
        else: #Si no ha ingresado la ciudad
            error = "Por favor, ingresa un nombre de ciudad." #Se indica que ingrese un nombre de ciudad   

    return render_template('index.html', data=weatherData, cityName=cityName, error=error) #Se retorna la plantilla index

#app route para mostrar el cv.html
@app.route('/cv')
def cv():
    return render_template('cv.html')  #Se Renderiza la plantilla del CV

if __name__ == "__main__":
    app.run(debug=True)