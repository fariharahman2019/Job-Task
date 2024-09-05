from . import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    hourly_rate = db.Column(db.Float)
    payment_verified = db.Column(db.Boolean, default=False)
    proposals = db.Column(db.Integer, default=0)
