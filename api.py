from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/citibike', methods=['GET'])
def get_citibike():
    return jsonify({'data': 5})

@app.route('/possible', methods=['GET'])
def get_possible():
    return jsonify({'data': 5})

@app.route('/selections', methods=['GET'])
def get_selections():
    k = request.args.get('k')
    return jsonify({'data': 5})

if __name__ == '__main__':
    app.run(debug=True)
