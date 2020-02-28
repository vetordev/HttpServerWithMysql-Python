from flask import Flask, jsonify, request

app = Flask(__name__)


devs = [
   {
      'id': 1,
      'name': 'Vitor da Silva',
      'lang': 'Python'
   },
   {
      'id': 2,
      'name': 'Vitoria Lopes',
      'lang': 'React JS'
   },
   {
      'id': 3,
      'name': 'Marcos Renato',
      'lang': 'Python'
   },
]

@app.route('/devs', methods=['GET'])
def dev():
   #Converte o objeto para json
   return jsonify(devs), 200
   pass

# Filtrar os devs por uma linguagem
@app.route('/devs/<string:lang>', methods=['GET'])
def dev_lang(lang):
   devs_per_language = [dev for dev in devs if dev['lang'] == lang]
   return jsonify(devs_per_language), 200
   pass

# Filtrar o dev pelo id
@app.route('/devs/<int:id>', methods=['GET'])
def devs_id(id):
   for dev in devs:
      if dev["id"] == id:
         return jsonify(dev), 200
   return jsonify({'error': 'dev not found'}), 404
   pass

# Inserindo um dev por meio do POST em json
@app.route('/devs', methods=['POST'])
def saveDev():
   data = request.get_json()
   devs.append(data)
   return jsonify(data), 201
   pass

# Alterando os dados de um dev
@app.route('/devs/<int:id>', methods=['PUT'])
def changeLang(id):
   new_lang = request.get_json().get('lang')
   for dev in devs:
      if dev['id'] == id:
         dev['lang'] = new_lang
         return jsonify(dev), 200
         pass
   return jsonify({'error': 'dev not found'}), 404
   pass

# Removendo um dev
@app.route('/devs/<int:id>', methods=['DELETE'])
def removeDev(id):
   index = id - 1
   del devs[index]
   return jsonify({'message': 'dev deleted with sucess'})
   
   pass
# Rota padrão da aplicação
# O método correspondente a rota deverá vir logo abaixo a declaração da rota
@app.route('/', methods=['GET'])
def index():
   return 'Hello', 200



if __name__ == '__main__':
   app.run(debug=True)   