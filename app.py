from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/')
def inde():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
       if request.method == 'POST':
           city = request.form['city']
           url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=4b1b50cb07362ff6018b15c5a0f87f56"
           r = requests.get(url).json()
           weather = {
               'city' : city,
               'temperature' : r['main']['temp'],
               'description' : r['weather'][0]['description']
           } 
           return render_template('index.html', weather=weather)
       else:
           return render_template('index.html')
       
if __name__ == '__main__':
     app.run(debug=True)