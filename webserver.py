from flask import Flask, jsonify, request

app = Flask(__name__)

languages = {'id' : 'JavaScript', 'data' : 'Python', 'type' : 'Ruby'}

@app.route('/', methods = ['GET'])

def test():
    return jsonify({'message' : 'It works!'})

@app.route('/', methods = ['POST'])
def transaction():
    input_path = request.json['path']
    print input_path

    languages['path'] = input_path
    return jsonify({'languages' : languages})

@app.route('/lang', methods = ['GET'])
def returnAll():
    return jsonify({'transaction' : languages})

@app.route('/lang/<string:name>', methods = ['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

@app.route('/lang', methods = ['POST'])
def addOne():
    language = {'test' : request.json['test']}

    languages.append(language)
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods = ['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language' : langs[0]})

@app.route('/lang/<string:name>', methods = ['DELETE'])
def removeOne(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'languages': language})


if __name__ == '__main__' :
    app.run(host="10.1.148.2", port=8080, threaded = True)