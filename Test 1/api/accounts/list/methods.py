from app import db
from utils.error_handler import CustomException
from utils.logger import log_info, log_error
from services.account_logic import AccountLogic
from flask import request
from .schemas import AccountListGetSchema
from api.base_resource import Resource

class AccountListResource(Resource):
    def get(self):
        logic = AccountLogic(db.session)

        try:
            log_info("Get all accounts (from list)")
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 10))
            accounts = logic.get_all_accounts(page, per_page)
            schema = AccountListGetSchema()
            result = schema.dump(accounts)

            return {'status': True, 'result': result}
        
        except CustomException as e:
            log_error(f"Error getting accounts (from list): {e.message}")
            return {'status': False, 'message': e.message}, e.status_code
        
        except Exception as e:
            log_error(f"Unexpected error getting accounts (from list): {e}")
            return {'status': False, 'message': 'Internal Server Error'}, 500