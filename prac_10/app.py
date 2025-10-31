from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/fahrenheit')
def convert_to_celsius(fahrenheit=23):
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    return str(celsius)


@app.route('/f/<celsius>')
def convert_to_fahrenheit(celsius=11):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return str(fahrenheit)


if __name__ == '__main__':
    app.run()

