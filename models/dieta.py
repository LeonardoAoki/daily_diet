from database import db
from flask_login import UserMixin

class Dieta(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_hora = db.Column(db.String(80), nullable=False)
    dentro_dieta = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descrição": self.descricao,
            "data e hora": self.data_hora,
            "dentro da dieta": self.dentro_dieta
        }