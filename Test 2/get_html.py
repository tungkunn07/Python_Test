from flask import Flask, request, jsonify
import os
import base64
import json

app = Flask(__name__)

def get_html_file_data(file, app_env, contract_app, contract_server):
    # Searches for and returns the Base64 encoded content of an HTML file based on parameters.
    base_path = "C:\\imprints_html_file"
    env_folders = {0: "AWS", 1: "K5", 2: "T2"}
    server_folders = {0: "app1", 1: "app2"}

    env_folder = env_folders.get(app_env)
    server_folder = server_folders.get(contract_server)

    if not env_folder or not server_folder:
        return {"success": False, "message": "Invalid app_env or contract_server value", "FileName": ""}

    file_path = os.path.join(base_path, env_folder, server_folder, f"{file}.html")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        encoded_content = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
        return {"success": True, "filename": f"{file}.html", "content": encoded_content, "message": "Seal Info response successfully"}
    except FileNotFoundError:
        return {"success": False, "message": f"File not found at: {file_path}", "FileName": ""}
    except Exception as e:
        return {"success": False, "message": f"An error occurred: {e}", "FileName": ""}

@app.route('/api/get_html_data', methods=['POST'])
def get_html_data_api():
    try:
        data = request.get_json()

        if not data or not all(key in data for key in ['file', 'app_env', 'contract_app', 'contract_server']):
            return jsonify({"success": False, "message": "Missing required parameters", "FileName": ""}), 400

        file_param = data.get('file')
        app_env_param = data.get('app_env')
        contract_app_param = data.get('contract_app')
        contract_server_param = data.get('contract_server')

        if not isinstance(file_param, str):
            return jsonify({"success": False, "message": "Invalid file parameter", "FileName": ""}), 400
        if not isinstance(app_env_param, int):
            return jsonify({"success": False, "message": "Invalid app_env parameter", "FileName": ""}), 400
        if not isinstance(contract_app_param, int):
            return jsonify({"success": False, "message": "Invalid contract_app parameter", "FileName": ""}), 400
        if not isinstance(contract_server_param, int):
            return jsonify({"success": False, "message": "Invalid contract_server parameter", "FileName": ""}), 400

        result = get_html_file_data(file_param, app_env_param, contract_app_param, contract_server_param)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e), "FileName": ""}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)