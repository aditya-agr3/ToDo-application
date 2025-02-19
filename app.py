from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Todo Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    completed = db.Column(db.Boolean, default=False)

def __init__(self, title, description, completed):
    self.title = title
    self.description = description
    self.completed = completed

# Todo Schema
class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

# Routes
@app.route('/todo', methods=['POST'])
def add_todo():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description', '')
        completed = data.get('completed', False)
        
        if not title:
            return jsonify({"error": "Title is required"}), 400

        new_todo = Todo(title=title, description=description, completed=completed)
        db.session.add(new_todo)
        db.session.commit()
        logger.info(f"Todo added: {title}")
        return todo_schema.jsonify(new_todo), 201
    except Exception as e:
        logger.error(f"Error adding todo: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/todo', methods=['GET'])
def get_todos():
    all_todos = Todo.query.all()
    return jsonify(todos_schema.dump(all_todos))

@app.route('/todo/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get(id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return todo_schema.jsonify(todo)

@app.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    try:
        todo = Todo.query.get(id)
        if not todo:
            return jsonify({"error": "Todo not found"}), 404
        
        data = request.get_json()
        todo.title = data.get('title', todo.title)
        todo.description = data.get('description', todo.description)
        todo.completed = data.get('completed', todo.completed)

        db.session.commit()
        logger.info(f"Todo updated: {id}")
        return todo_schema.jsonify(todo)
    except Exception as e:
        logger.error(f"Error updating todo: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    try:
        todo = Todo.query.get(id)
        if not todo:
            return jsonify({"error": "Todo not found"}), 404
        
        db.session.delete(todo)
        db.session.commit()
        logger.info(f"Todo deleted: {id}")
        return jsonify({"message": "Todo deleted successfully"})
    except Exception as e:
        logger.error(f"Error deleting todo: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Run Server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
