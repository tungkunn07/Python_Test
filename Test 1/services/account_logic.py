from models.account import Account
from utils.error_handler import CustomException
from utils.logger import log_info, log_error

class AccountLogic:
    def __init__(self, session):
        self.session = session

    def get_all_accounts(self, page, per_page):
        log_info(f"Getting all accounts, page: {page}, per_page: {per_page}")

        return Account.query.paginate(page=page, per_page=per_page)

    def get_account_by_id(self, account_id):
        log_info(f"Getting account by ID: {account_id}")
        account = Account.query.get(account_id)

        if not account:
            log_error(f"Account with ID {account_id} not found")
            return None
        
        return account

    def create_account(self, account_data):
        log_info(f"Creating new account: {account_data}")
        account = Account(**account_data)
        self.session.add(account)
        self.session.commit()

        return account

    def update_account(self, account_id, account_data):
        log_info(f"Updating account with ID {account_id}, data: {account_data}")
        account = self.get_account_by_id(account_id)

        if not account:
            return None
        
        for key, value in account_data.items():
            setattr(account, key, value)

        self.session.commit()
        return account

    def delete_account(self, account_id):
        log_info(f"Deleting account with ID: {account_id}")
        account = self.get_account_by_id(account_id)

        if not account:
            return False
        
        self.session.delete(account)
        self.session.commit()
        return True