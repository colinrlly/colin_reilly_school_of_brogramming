import functools
from app.helper.calc import Calculator

from flask import request, make_response
from app.helper.db import get_db
from app.api import api_bp


@api_bp.route('/calculate', methods=['POST'])
def calculate():
    calc = Calculator()
    data = request.json

    try:
        equation = data['to_calculate']
        result = calc.calculate(equation)
    except KeyError:
        return make_response({"error": "Missing required parameter 'to_caclulate'"}, 400)
    except Exception as e:
        return make_response({"error": "Could not process equation", "reason": str(e)}, 400)

    try:
        db = get_db()
        db.execute(
            "INSERT INTO calculate_history (input, result) VALUES (?, ?)",
            (equation, result)
        )
        db.commit()
    except:
        return make_response({'error': "Error accessing backing database"}, 500)

    return make_response({'result': result}, 200)
