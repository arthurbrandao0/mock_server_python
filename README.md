# Mock Server in Python using Flask

This project provides a simple example of creating a mock server in Python using the Flask framework. A mock server is useful for simulating API endpoints during software development and testing.

## Installation

Make sure you have Python and pip installed. Then, install the dependencies using the following command:

```bash
pip install flask
```

## Usage
Clone the repository:
```bash
git clone https://github.com/your-username/mock-server-flask.git
cd mock-server-flask
```
1. Run the mock server:
```bash
python mock_server.py
```
The server will start on port 5000 by default.

## Available Routes
### Example without Parameters
- Route: **/api/example**
- Method: **GET**
- Response: Returns a sample JSON.

###Example with Parameter
- Route: **/api/example/<parameter>**
- Method: **GET**
- Response: Returns a JSON that includes the provided parameter.

Example: Access **http://localhost:5000/api/example/123** to see the response with the parameter "123".