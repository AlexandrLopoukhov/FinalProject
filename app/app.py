from config import app
from controllers.compound_controller import api

# register the api
app.register_blueprint(api)


if __name__ == '__main__':
    '''run application'''
    app.run(host='127.0.0.1', port=5000)
