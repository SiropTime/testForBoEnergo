import logging
import sys

from flask import Blueprint, request, abort, Response


api = Blueprint('api', __name__)

logger = logging.getLogger(__name__)

handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(format='[%(asctime)s %(levelname)s]:%(message)s', handlers=[handler], level=logging.DEBUG)


@api.route("/solution", methods=['GET'])
def process_solution():
    # JSON is like {"a": float, "b": float, "c": float}
    try:
        try:
            data = request.get_json()
        except Exception as ex:
            logger.warn("There's no JSON from client | Request body: ", request.data)
            return abort(Response(str(ex), 400))
        try:
            a, b, c = (data[k] for k in ('a', 'b', 'c'))
        except KeyError as ex:
            logger.warn("Wrong format of JSON from client | Request JSON: ", data)
            raise Exception(f"'{ex.args[0]}' is required")
    except Exception as ex:
        logger.error("Something went wrong | ", ex)
        return abort(Response(str(ex), 400))

    # Calculating D
    d = b**2 - 4*a*c
    if d < 0:
        return {"answer": []}
    elif d == 0:
        try:
            answer = -(b/2*a)
        except ZeroDivisionError:
            logger.error("ZeroDivisionError, check variables")
            return abort(Response("ZeroDivisionError, check variables", 406))
        return {"answer": [answer]}
    else:
        try:
            answers = [(-b+d**(1/2))/(2*a), (-b-d**(1/2))/(2*a)]
        except ZeroDivisionError:
            logger.error("ZeroDivisionError, check variables")
            return abort(Response("ZeroDivisionError, check variables", 406))
        return {"answer": answers}
