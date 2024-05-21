#!/usr/bin/python3

from models import User
from server.api.views import app_views
from flask import Blueprint,  Flask,  request
from flask_restx import Api, Resource, fields
app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == '__main__':
    app.run(debug=True)