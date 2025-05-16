from flask import Flask
from flask_mail import Mail
from app.routes import main
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'reach2nishchhal@gmail.com'  # replace with your email
app.config['MAIL_PASSWORD'] = 'Mr.Hunt@2601'     # replace with your app password

mail = Mail(app)

# Register blueprint
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
