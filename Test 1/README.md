# --- Requirement --- 
- There is the below table in the database
- Develop the CRUD APIs (create/update/delete/get all with pagination/get one) for this table.
- All APIs must to have data validation, exception handling and logging.

# --- How to Run ---
1. Open terminal or command prompt: Navigate to the folder where I saved the Python file.
2. Install Python and Pip: Make sure you have Python and Pip installed on your computer.
3. Create and activate virtual environments
    ```
        python -m venv venv
        venv\Scripts\activate  # In Windows
    ```
4. Install the required libraries:
    ```pip install -r requirements.txt```
5. Create a database and run migrations (if applicable): If you are using a database like MySQL or PostgreSQL, create the database first. Then, run the following command to create the tables:
    ```
        flask db init
        flask db migrate -m "Initial migration"
        flask db upgrade
    ```
6. Run Flask application
    ```python app.py```
7. Use ping.py to test the API: Open a new terminal and run the ping.py script
    ```python ping.py```