from db import db


class ExpiredTokenModel(db.Model):
    __tablename__ = "expired_token"

    token = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)