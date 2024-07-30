from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class info_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wmname = db.Column(db.String(50), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    host = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Wm_name(wmname='{self.name}', company_name='{self.company_name}', status='{self.status}', address='{self.address}', host='{self.host}')"
