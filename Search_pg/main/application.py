from flask import Flask

# create the extension

# create the app
app = Flask(__name__,template_folder='templates',static_folder='static')


def create_app():
    from Search_pg.client.controller import client
    from Search_pg.user.controller import user
    from Search_pg.login.controller import validate
    from Search_pg.login.administation import admin
    app.register_blueprint(validate)
    app.register_blueprint(client)
    app.register_blueprint(user)
    app.register_blueprint(admin)
    return app

