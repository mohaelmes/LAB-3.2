from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configuración de la aplicación
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos
db = SQLAlchemy(app)

# Definición del modelo
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Crear todas las tablas al iniciar la aplicación
with app.app_context():
    db.create_all()

# Ruta principal
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API REST con SQLite"})

# Obtener todos los elementos
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name, "description": item.description} for item in items])

# Obtener un elemento por ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item no encontrado"}), 404
    return jsonify({"id": item.id, "name": item.name, "description": item.description})

# Crear un nuevo elemento
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    if not data or not data.get('name'):
        return jsonify({"error": "El nombre es requerido"}), 400
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item creado", "item": {"id": new_item.id, "name": new_item.name, "description": new_item.description}}), 201

# Actualizar un elemento por ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item no encontrado"}), 404
    data = request.json
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    db.session.commit()
    return jsonify({"message": "Item actualizado", "item": {"id": item.id, "name": item.name, "description": item.description}})

# Eliminar un elemento por ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item no encontrado"}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item eliminado"})

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
