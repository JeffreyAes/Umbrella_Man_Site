from flask_app import app
from flask_app.controllers import user_controller
from flask_app.controllers import dashboard_controller
# ...server.py



if __name__ == "__main__":
    app.run(debug=True)