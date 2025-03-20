from flask import jsonify

class CustomException(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

def handle_exception(e):
    if isinstance(e, CustomException):
        response = jsonify({'error': e.message})
        response.status_code = e.status_code
        return response
    else:
        # Log the unexpected error
        print(f"Unexpected error: {e}")
        response = jsonify({'error': 'Internal Server Error'})
        response.status_code = 500
        return response