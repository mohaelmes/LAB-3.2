from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definición del modelo de la base de datos
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def as_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}

# Crear la base de datos al inicio de la aplicación
@app.before_first_request
def create_tables():
    db.create_all()

# Método para obtener todos los items
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([item.as_dict() for item in items])

# Método para agregar un nuevo item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.as_dict()), 201

# Método para obtener un item por ID
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(item.as_dict())

# Método para actualizar un item por ID
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    item.name = data['name']
    item.description = data.get('description')
    db.session.commit()
    return jsonify(item.as_dict())

# Método para eliminar un item por ID
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted'}), 200

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
