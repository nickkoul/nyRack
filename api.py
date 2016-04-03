import main, learn, json
from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('map.html')

@app.route('/citibike', methods=['GET'])
def get_citibike():
    citi_nodes = main.get_citiBike_stations()
    citi_nodes = list(map(lambda tuple: (tuple[0].node.location[1],
                                         tuple[0].node.location[0]), citi_nodes))
    return json.dumps(citi_nodes)

@app.route('/new', methods=['GET'])
def get_new():
    new_nodes = main.read_new_nodes()
    new_nodes = list(map(lambda node: (node.location[1],
                                       node.location[0]), new_nodes))
    return json.dumps(new_nodes)

@app.route('/existing', methods=['GET'])
def get_existing():
    existing_nodes = main.read_exisiting_nodes()
    existing_nodes = list(map(lambda node: (node.location[1],
                                            node.location[0]), existing_nodes))
    return json.dumps(existing_nodes)

@app.route('/k', methods=['GET'])
def k():
    k = int(request.args.get('k'))
    n = int(request.args.get('n'))
    k_new_nodes = main.get_k_new_stations(n)
    k_new_nodes = list(map(lambda node: (node.location[1],
                                         node.location[0]), k_new_nodes))
    return json.dumps(k_new_nodes)

if __name__ == '__main__':
    app.run(debug=True)
