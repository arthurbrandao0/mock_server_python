# Mock Server in Python using Flask

This project provides a simple example of creating a mock server in Python using the Flask framework. A mock server is useful for simulating API endpoints during software development and testing.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/arthurbrandao0/mock_server_python.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd mock-server-flask
    ```

3. **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
   ```
   
## Running the mock server

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