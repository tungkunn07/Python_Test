from app import db
from utils.error_handler import CustomException
from utils.logger import log_info, log_error
from services.account_logic import AccountLogic
from flask import request
from .schemas import AccountGetSchema, AccountPostSchema, AccountPatchSchema, AccountDeleteSchema
from api.base_resource import Resource

class AccountsResource(Resource):
    def get(self, account_id):
        logic = AccountLogic(db.session)

        try:
            data = request.get_json()
            schema = AccountGetSchema()
            errors = schema.validate(data)

            if errors:
                raise CustomException(errors, 400)
            
            log_info(f"Get account with ID: {account_id}")
            account = logic.get_account_by_id(account_id)

            if not account:
                raise CustomException("Account not found", 404)
            
            return {'status': True, 'result': account}
        
        except CustomException as e:
            log_error(f"Error getting account: {e.message}")
            return {'status': False, 'message': e.message}, e.status_code
        
        except Exception as e:
            log_error(f"Unexpected error getting account: {e}")
            return {'status': False, 'message': 'Internal Server Error'}, 500

    def post(self):
        logic = AccountLogic(db.session)

        try:
            data = request.get_json()
            schema = AccountPostSchema()
            errors = schema.validate(data)

            if errors:
                raise CustomException(errors, 400)
            
            log_info(f"Creating account with data: {data}")
            account = logic.create_account(data)

            return {'status': True, 'result': account}, 201
        
        except CustomException as e:
            log_error(f"Error creating account: {e.message}")
            return {'status': False, 'message': e.message}, e.status_code
        
        except Exception as e:
            log_error(f"Unexpected error creating account: {e}")
            return {'status': False, 'message': 'Internal Server Error'}, 500

    def patch(self, account_id):
        logic = AccountLogic(db.session)

        try:
            data = request.get_json()
            schema = AccountPatchSchema()
            errors = schema.validate(data)

            if errors:
                raise CustomException(errors, 400)
            
            log_info(f"Updating account {account_id} with data: {data}")
            account = logic.update_account(account_id, data)

            if not account:
                raise CustomException("Account not found", 404)
            
            return {'status': True, 'result': account}
        
        except CustomException as e:
            log_error(f"Error updating account: {e.message}")
            return {'status': False, 'message': e.message}, e.status_code
        
        except Exception as e:
            log_error(f"Unexpected error updating account: {e}")
            return {'status': False, 'message': 'Internal Server Error'}, 500

    def delete(self, account_id):
        logic = AccountLogic(db.session)

        try:
            data = request.get_json()
            schema = AccountDeleteSchema()
            errors = schema.validate(data)

            if errors:
                raise CustomException(errors, 400)
            
            log_info(f"Deleting account {account_id}")
            success = logic.delete_account(account_id)

            if not success:
                raise CustomException("Account not found", 404)
            
            return {'status': True, 'message': 'Account deleted'}
        
        except CustomException as e:
            log_error(f"Error deleting account: {e.message}")
            return {'status': False, 'message': e.message}, e.status_code
        
        except Exception as e:
            log_error(f"Unexpected error deleting account: {e}")
            return {'status': False, 'message': 'Internal Server Error'}, 500