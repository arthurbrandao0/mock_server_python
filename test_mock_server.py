import unittest
import requests

class TestMockServerAPI(unittest.TestCase):
    base_url = "http://localhost:5000"

    def test_example_route(self):
        response = requests.get(f"{self.base_url}/api/example")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'This is an example response from the mock server')

    def test_example_with_parameter_route(self):
        parameter_value = '123'
        response = requests.get(f"{self.base_url}/api/example/{parameter_value}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], f'You provided the parameter: {parameter_value}')

if __name__ == '__main__':
    unittest.main()
