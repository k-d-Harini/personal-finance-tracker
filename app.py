from flask import Flask, render_template

from config import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)

# Create database tables
with app.app_context():
    import models  # Import models so SQLAlchemy knows about them before creating tables
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
