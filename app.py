from flask import Flask, render_template

app = Flask(__name__)

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

if __name__=="__main__":
    app.run(debug=True, port=8080)
