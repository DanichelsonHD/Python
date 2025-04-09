from flask import Flask, request, jsonify
from read_data import sum_by_type  # Importe a função do seu arquivo Python

app = Flask(__name__)

@app.route('/sum_by_type', methods=['POST'])
def get_sum_by_type():
    data = request.json  # Recebe os dados enviados pelo AJAX
    category = data.get('category')  # Obtém o parâmetro 'category'
    result = sum_by_type(category)  # Chama a função Python
    return jsonify({'result': result})  # Retorna o resultado como JSON

if __name__ == '__main__':
    app.run(debug=True)