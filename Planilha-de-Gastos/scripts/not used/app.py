from flask import Flask, request, jsonify
from flask_cors import CORS
from read_data import sum_by_type

app = Flask(__name__)
CORS(app)

@app.route('/sum_by_type', methods=['POST'])
def get_sum_by_type():
    data = request.json
    category = data.get('category')
    result = sum_by_type(category)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)