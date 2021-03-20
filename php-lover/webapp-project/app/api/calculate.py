import functools
from app.helper.calc import Calculator

from flask import request, make_response, flash, render_template
from app.helper.db import get_db
from app.api import api_bp


@api_bp.route('/calculate', methods=['GET', 'POST'])
def calculate():
    calc = Calculator()
    use_json = request.method == 'POST'

    data = request.json if use_json else request.args

    error = "Could not process equation"
    error_code = None
    result = None

    try:
        equation = data['to_calculate']
        result = calc.calculate(equation)
    except KeyError:
        reason = "Missing required parameter 'to_caclulate'"
        error_code = 400
        flash(f"{error}: reason")
    except Exception as e:
        reason = str(e)
        error_code = 400
        flash(f"{error}: {reason}")

    try:
        db = get_db()
        db.execute(
            "INSERT INTO calculate_history (input, result) VALUES (?, ?)",
            (equation, result)
        )
        db.commit()
    except Exception as e:
        reason = "Error accessing backing database"
        error_code = 500
        flash(f"{error}: {reason}")

    if use_json:
        if error_code:
            return make_response({"error": error, "reason": reason}, error_code)
        return make_response({'result': result}, 200)

    return render_template('calculate.html.jinja', result=result)
