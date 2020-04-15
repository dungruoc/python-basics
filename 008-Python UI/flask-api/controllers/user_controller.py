from flask import request
from flask_restplus import Resource
from flask_restplus import Namespace, fields

user_api = Namespace('user', description='user related operations')

user_model = user_api.model('user', {
  'id': fields.String(required=True, description='user id'),
  'email': fields.String(required=True, description='user email address'),
  'username': fields.String(required=True, description='user username')
})

@user_api.route('/')
class UserList(Resource):

    # @user_api.doc('list_of_registered_users')
    # @user_api.expect(parser)
    @user_api.marshal_list_with(user_model, envelope='data')
    def get(self):
        """List all registered users"""
        return [
          {
            'id': '1',
            'email': 'hehe@gmail.com',
            'username': 'Hehe Python'
          },
          {
            'id': '2',
            'email': 'hehe2@gmail.com',
            'username': 'Hehe2 Python'
          }
        ]
