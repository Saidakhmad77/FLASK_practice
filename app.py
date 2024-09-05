from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def get_countries():
    with open("countries.json", 'r') as file:
        countries_data = json.load(file)
    return countries_data
"""     return json.loads(countries_data) """

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/home')
def homepage():
    return render_template('index.html')

@app.route('/homepage')
def get_homepage():
    return render_template('hello.html')

@app.route('/hello')
def hello():
    return '<p>Hello, World</p>'

@app.route('/goodbye')
def goodbye():
    x = create_title()
    return x

def create_title():
    return '<p>Title page</p>'


@app.route("/countries")
def get_country_html():
    countries = get_countries()
    print(countries)
    return render_template("countries.html", countries=countries)


@app.route("/api/countries")
def get_country():
    countries = get_countries()
    return jsonify(countries)


if __name__=="__main__":
    app.run(debug=True, port=8080)
    
    
    
