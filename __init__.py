from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)

    # Email configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your.email@gmail.com'        # Replace with your Gmail
    app.config['MAIL_PASSWORD'] = 'your-app-password'           # Use Gmail App Password

    mail.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
