from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')  # Get the 'name' parameter, default to 'World'
    response = make_response(
        {
            'response': f'Hello, {name}!',
            'status': 200
        }
    )
    return response

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="healthy"), 200  # Standard health check response

if __name__ == '__main__':
    # Run Flask app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

