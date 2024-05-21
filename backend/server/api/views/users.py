from server.api.views import api
from flask_restx import fields, Resource, reqparse
from models import User
from flask import request

response = {
    200: 'success',
    404: 'not found'
}
users = api.model('Users', {
    'name': fields.String,
    'age' : fields.Integer,
    'links' : fields.List(fields.String),
    'created_at' : fields.DateTime
})
user = api.model( 'User', {
    'name': fields.String,
    'age' : fields.Integer,
    'links' : fields.List(fields.String),
    'created_at' : fields.DateTime
    }
)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, location= ('json'), help = 'id of the instance')


@api.route('/user/')
class Users(Resource):
    @api.marshal_with(users, envelope='users')
    @api.doc(responses=response)
    def get(self):
        return User.all()

    @api.marshal_with(user, envelope='user')
    @api.doc(parser=parser, responses=response) 
    def post(self):
        args = parser.parse_args()
        id = args['id']
        return User.get(id)
