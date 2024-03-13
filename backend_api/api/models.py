from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mercadoria(db.Model):
    __tablename__ = 'mercadorias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero_registro = db.Column(db.String(25), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricantes.id'), nullable=False)
    fabricante = db.relationship("Fabricante", back_populates="mercadorias")
    mercadoria_tipo_id  = db.Column(db.Integer, db.ForeignKey('mercadoria_tipos.id'), nullable=False)
    mercadoria_tipo = db.relationship("Mercadoria_Tipo", back_populates="mercadorias")
    descricao = db.Column(db.String(255), nullable=False)
    deletado = db.Column(db.Boolean, default=False, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'numero_registro': self.numero_registro,
            'fabricante_id': self.fabricante_id,
            'fabricante_nome': self.fabricante.nome,
            'mercadoria_tipo_id': self.mercadoria_tipo_id,
            'mercadoria_tipo_nome': self.mercadoria_tipo.nome,
            'descricao': self.descricao,
        }

class Fabricante(db.Model):
    __tablename__ = 'fabricantes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    mercadorias = db.relationship("Mercadoria", back_populates="fabricante")

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }

class Mercadoria_Tipo(db.Model):
    __tablename__ = 'mercadoria_tipos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    mercadorias = db.relationship("Mercadoria", back_populates="mercadoria_tipo")

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }

class Mercadoria_Movimentacao(db.Model):
    __tablename__ = 'mercadoria_movimentacoes'
    id = db.Column(db.Integer, primary_key=True)
    mercadoria_local_id = db.Column(db.Integer, db.ForeignKey('mercadoria_locais.id'), nullable=False)
    mercadoria_local = db.relationship("Mercadoria_Local", back_populates="mercadoria_movimentacoes")
    data_hora = db.Column(db.DateTime(), nullable=False)
    mercadoria_id = db.Column(db.Integer, db.ForeignKey('mercadorias.id'), nullable=False)
    mercadoria = db.relationship('Mercadoria', backref=db.backref('movimentacoes', lazy=True))
    quantidade = db.Column(db.Integer, nullable=False)

    def to_dict(self):
       return {
            'id': self.id,
            'data_hora': self.data_hora.strftime("%Y-%m-%d %H:%M:%S"),
            'mercadoria_id': self.mercadoria_id,
            'quantidade': self.quantidade,
            'local_id': self.local_id,
            'local_nome': self.local.nome,
        }

class Mercadoria_Local(db.Model):
    __tablename__ = 'mercadoria_locais'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    
    mercadoria_movimentacoes = db.relationship("Mercadoria_Movimentacao", back_populates="mercadoria_local")

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }
