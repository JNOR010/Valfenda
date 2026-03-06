from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API está funcionando!"})

@app.route('/api/dados', methods=['GET'])
def get_dados():
    return jsonify({
        "status": "sucesso",
        "dados": ["item1", "item2", "item3"]
    })

@app.route('/api/dados', methods=['POST'])
def post_dados():
    data = request.get_json()
    return jsonify({
        "status": "recebido",
        "dados_enviados": data
    }), 201

@app.route('/api/usuario/<nome>')
def get_usuario(nome):
    return jsonify({
        "usuario": nome,
        "mensagem": f"Olá, {nome}!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
