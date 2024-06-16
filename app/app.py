from flask import Flask, jsonify, request
from waitress import serve

from script_loader import ScriptLoader

port = 55001

app = Flask(__name__)

script_manager = ScriptLoader()


@app.route("/")
def health():
    return '', 200


@app.route("/load", methods=['POST'])
def load_script():
    res, message = script_manager.load_script(module_name=request.json['module'], path=request.json['path'])

    if not res:
        return jsonify({'result': res, 'message': message}), 400

    return jsonify({'result': res, 'message': ''}), 200


@app.route("/unload", methods=['GET'])
def unload_script():
    script_manager.unload_script()
    return '', 200


@app.route('/script/home', methods=['GET'])
def get_home_page():
    if not script_manager.is_loaded():
        return jsonify({'error': 'Script manager not loaded'}), 404
    result, data = script_manager.get_home_page()
    if result:
        return jsonify(data), 200
    else:
        return jsonify({'error': data}), 400


@app.route('/script/search', methods=['POST'])
def search_page():
    if not script_manager.is_loaded():
        return jsonify({'error': 'Script manager not loaded'}), 404

    # Access query parameters
    # query = request.args.get('query')  # Single parameter
    # page = request.args.get('page', default=1, type=int)  # Single parameter with a default value and type

    # todo
    return jsonify({'error': 'unimplemented'}), 404

    # return jsonify(script_manager.get_home_page()), 200


# app route for getting more info
# @app.route('/script/info', methods=['GET'])
# def search_page():
#     if not script_manager.is_loaded():
#         return jsonify({'error': 'Script manager not loaded'}), 404
#     return jsonify({'error': 'unimplemented'}), 404
#     # return jsonify(script_manager.get_home_page()), 200


# lmao this kills the app leaving this here, so you don't try that again
# @app.route("/quit", methods=['GET'])
# def quit_script():
#     os.kill(os.getpid(), signal.SIGTERM)
#     return None

# script specific commands


serve(app, host="0.0.0.0", port=port)
