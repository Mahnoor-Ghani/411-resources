from flask import Flask, request, jsonify, make_response
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    response = make_response(
        {
            'response': f'Hello, {name}!',
            'status': 200
        }
    )
    return response

@app.route('/repeat', methods=['GET'])
def repeat():
    input_value = request.args.get('input', '')
    return jsonify({'body': input_value, 'status': 200})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'body': 'OK', 'status': 200})

if __name__ == '__main__':
    port = os.getenv('PORT', 5000)  
    app.run(host='0.0.0.0', port=int(port), debug=True)

