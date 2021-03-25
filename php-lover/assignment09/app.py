from flask import Flask, request, make_response
from calc import Calculator
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/api/calculate', methods=['POST'])
def caclulate():
    calc = Calculator()
    data = request.json
    try:
        equation = data['to_calculate']
        result = calc.calculate(equation)
    except KeyError:
        return make_response({"error": "Missing required parameter 'to_caclulate'"}, 400)
    except:
        return make_response({"error": "Could not process equation"}, 400)

    return make_response({'result': result}, 200)
