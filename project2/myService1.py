from flask import jsonify, current_app


@current_app.route('/first', methods=['GET'])
def first_get():
    return jsonify({"message": "my first get service"})