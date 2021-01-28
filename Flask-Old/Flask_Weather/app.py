# python flask weather app
# uses openweeathermap.org - free api (bc the subs are $$$$$$$)

import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']

    api_key = get_api_key()
    data = get_weather_results(zip_code, api_key)

    # temperature stuff
    temp = data["main"]["temp"]
    temp_far = "{0:.2f}".format(data["main"]["temp"])
    temp_conv = (temp - 32) * (5/9)
    temp_celcius = "{0:.2f}".format(temp_conv)
    temp_feels = data["main"]["feels_like"]
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    feels_like_c = (temp_feels - 32) * (5/9)
    feels_conv = "{0:.2f}".format(feels_like_c)

    # descriptive stuff
    weather_desc = data["weather"][0]["main"]  # weather is array, grab 1st val
    weather_detail = data["weather"][0]["description"]
    # icon = data["weather"][0]["icon"]
    # how to icon?
    location = data["name"]
    humidity = data["main"]["humidity"]
    # grab some other neat info? sunset sunrise etc etc



    return render_template('results.html', temp=temp_far, temp_celcius=temp_celcius, feels_like=feels_like,
                           weather_desc = weather_desc, location=location, feels_conv = feels_conv,
                           weather_detail = weather_detail, humidity = humidity)


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_results(zip_code, api_key):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&units=imperial&appid" \
              f"={api_key}"
    r = requests.get(api_url)
    return r.json()


# run once
if __name__ == '__main__':
    app.run(debug=True)
