import requests

BASE_URL = "http://127.0.0.1:5005"

def ping_get_accounts():
    response = requests.get(f"{BASE_URL}/accounts/list")
    print("GET /accounts:", response.status_code)
    print(response.json())

def ping_get_account(account_id):
    response = requests.get(f"{BASE_URL}/accounts/{account_id}")
    print(f"GET /accounts/{account_id}:", response.status_code)
    print(response.json())

def ping_create_account(data):
    response = requests.post(f"{BASE_URL}/accounts", json=data)
    print("POST /accounts:", response.status_code)
    print(response.json())

def ping_update_account(account_id, data):
    response = requests.put(f"{BASE_URL}/accounts/{account_id}", json=data)
    print(f"PATCH /accounts/{account_id}:", response.status_code)
    print(response.json())

def ping_delete_account(account_id):
    response = requests.delete(f"{BASE_URL}/accounts/{account_id}")
    print(f"DELETE /accounts/{account_id}:", response.status_code)
    print(response.json())

if __name__ == "__main__":
    # Test GET all
    ping_get_accounts()

    # Test POST
    new_account_data = {
        "login": "test_user",
        "password": "test_password",
        "phone": "123456789"
    }
    ping_create_account(new_account_data)

    # Test GET one (assuming the new account has registerID 1)
    ping_get_account(1)

    # Test PATCH
    update_data = {
        "phone": "987654321"
    }
    ping_update_account(1, update_data)

    # Test GET one again to see the update
    ping_get_account(1)

    # Test DELETE
    ping_delete_account(1)

    # Test GET one after delete
    ping_get_account(1)