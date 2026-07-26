from flask import Flask
from models import init_db
from product.route import product_bp
from auth.route import auth_bp

app = Flask(__name__)
app.secret_key = 'lslsdo***'


init_db()


app.register_blueprint(product_bp)
app.register_blueprint(auth_bp)


app.run(debug= True)
