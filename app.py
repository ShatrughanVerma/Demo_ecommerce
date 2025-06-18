
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Product, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
CORS(app)

@app.before_first_request
def setup():
    init_db()

@app.route('/api/products', methods=['GET'])
def get_products():
    query = request.args.get('q', '')
    results = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
    return jsonify([p.to_dict() for p in results])

if __name__ == '__main__':
    app.run(debug=True)
