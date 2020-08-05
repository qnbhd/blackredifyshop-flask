from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Laptop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    img = db.Column(db.Text())
    description = db.Column(db.Text())
    year = db.Column(db.Integer)
    processor = db.Column(db.Text())
    color = db.Column(db.Text())
    storage = db.Column(db.String(16))


# db.create_all()


@app.route('/')
def index_page():
    query = Laptop.query
    count = query.count()
    random_laptop = randint(1, count)
    all_laptops = query.all()
    response = render_template('index.html', your_laptop=random_laptop, all_laptops=all_laptops)
    return response


@app.route('/<int:laptop_id>')
def laptop_page(laptop_id=-1):
    try:
        query_laptop_by_id = Laptop.query.filter_by(id=laptop_id)
        current_laptop = query_laptop_by_id[0]
        response = render_template('laptop.html', laptop=current_laptop)
    except IndexError:
        response = '404 not found', 404
    return response


app.run('localhost', 8080, debug=True)
