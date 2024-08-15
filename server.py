from Engine import createVectorDB, searchDB
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# CORS(app)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    query = data.get('query')
    DB = createVectorDB()
    results = searchDB(str(query), DB)
    return jsonify(results)

@app.route('/home', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query')
    DB = createVectorDB()
    results = searchDB(query, DB)
    #render a page and pass the results to display there
    pass

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
