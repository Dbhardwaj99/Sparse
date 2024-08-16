from Engine import createVectorDB, searchDB
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# CORS(app)

@app.route('/api', methods=['POST'])
def api():
    # data = request.get_json()
    # query = data.get('query')
    query = request.form['query']
    DB = createVectorDB()
    results = searchDB(str(query), DB)

    #create a json file to save this data
    with open('data.json', 'w') as f:
        json.dump(results, f)

    return jsonify(results)

@app.route('/home', methods=['POST'])
def search():
    # data = request.get_json()
    # query = data.get('query')
    query = request.form['query']
    DB = createVectorDB()
    results = searchDB(query, DB)

    with open('data.json', 'w') as f:
        json.dump(results, f)

    #render a page and pass the results to display there
    return render_template('index.html', results=results, query=query)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
