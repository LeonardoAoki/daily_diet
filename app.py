from flask import Flask, request, jsonify
from models.dieta import Dieta
from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    data = request.json
    nome = data.get("nome")
    descricao = data.get("descrição")
    data_hora = data.get("data e hora")
    dentro_dieta = data.get("dentro da dieta")

    if nome:
        dieta = Dieta(nome=nome, descricao=descricao, data_hora=data_hora, dentro_dieta=dentro_dieta)
        db.session.add(dieta)
        db.session.commit()
        return jsonify({"message": "Refeição cadastrada com sucesso!"})
    
    return jsonify({"message": "Dados inválidos"}), 400

@app.route("/editar/<int:id_refeicao>", methods=["PUT"])
def editar(id_refeicao):
    data = request.json
    dieta = Dieta.query.get(id_refeicao)

    if dieta:
        dieta.nome = data.get("nome")
        dieta.descricao = data.get("descrição")
        dieta.data_hora = data.get("data e hora")
        dieta.dentro_dieta = data.get("dentro da dieta")
        db.session.commit()

        return jsonify({"message": f"Refeição {id_refeicao} atualizada com sucesso!"})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/deletar/<int:id_refeicao>", methods=["DELETE"])
def deletar(id_refeicao):
    dieta = Dieta.query.get(id_refeicao)

    if dieta:
        db.session.delete(dieta)
        db.session.commit()
        return jsonify({"message": f"Refeição {id_refeicao} deletada com sucesso!"})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/listar", methods=["GET"])
def listar_refeicoes():
    refeicoes = Dieta.query.all()
    return jsonify([refeicao.to_dict() for refeicao in refeicoes])

@app.route("/listar/<int:id_refeicao>", methods=["GET"])
def listar_refeicao(id_refeicao):
    dieta = Dieta.query.get(id_refeicao)

    if dieta:
        return {"id": dieta.id,
                "nome": dieta.nome,
                "descrição": dieta.descricao,
                "data e hora": dieta.data_hora,
                "dentro da dieta": dieta.dentro_dieta
                }
    
    return jsonify({"message": "Refeição não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)