from flask import Blueprint
from flask_restx import Api

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
api = Api(app_views)

from server.api.views.users import Users
