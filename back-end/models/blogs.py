from db import db


class Blogs(db.Model):
    __tablename__ = "Blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    Contenu = db.Column(db.String, nullable=False)