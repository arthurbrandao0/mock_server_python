from flask import Flask, jsonify

app = Flask(__name__)

# Example route that returns a JSON response
@app.route('/api/example', methods=['GET'])
def example():
    mock_data = {'message': 'This is an example response from the mock server'}
    return jsonify(mock_data)

# Example route with parameter
@app.route('/api/example/<parameter>', methods=['GET'])
def example_with_parameter(parameter):
    mock_data = {'message': f'You provided the parameter: {parameter}'}
    return jsonify(mock_data)

# Run the server on port 5000
if __name__ == '__main__':
    app.run(port=5000)
