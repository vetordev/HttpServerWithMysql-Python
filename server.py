from flask import Flask, jsonify, request
import mysqldb

con = mysqldb.createConnection('root', '', 'localhost', 'devdb')

app = Flask(__name__)

@app.route('/dev', methods=['GET'])
def findAllDev():
   query = 'SELECT * FROM `dev`'
   rows = mysqldb.selectAll(query, con)
   return jsonify(rows)
   pass

@app.route('/dev', methods=['POST'])
def createDev():
   data = request.get_json()
   mysqldb.create(data, con)
   return jsonify(data), 200
   pass

@app.route('/dev/<int:dev_id>', methods=['PUT'])
def alterDev(dev_id):
   data = request.get_json()
   data['dev_id'] = dev_id
   mysqldb.alter(data, con)
   return jsonify(data), 200
   pass

@app.route('/dev/<int:dev_id>', methods=['DELETE'])
def deleteDev(dev_id):
   data = {'dev_id': dev_id}
   mysqldb.delete(data, con)
   return jsonify(''), 200
   pass
if __name__ == '__main__':
   app.run(debug=True)
   pass