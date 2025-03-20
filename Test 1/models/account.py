from app import db

class Account(db.Model):
    __tablename__ = 'accounts'

    registerID = db.Column(db.Integer, primary_key=True, autoincrement=True, unsigned=True, nullable=False, default=0)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(20))

    def __repr__(self):
        return f"<Account(registerID={self.registerID}, login='{self.login}')>"