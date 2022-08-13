from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from pprint import pprint
from flask_app.models.painting import Painting

DATABASE = 'paintings'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.paintings = []
    
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    ## ! used in user validation
    @classmethod
    def get_by_email(cls,data:dict) -> object or bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    ##! get all of a user's paintings
    @classmethod 
    def get_user_with_paintings(cls, data):
        query = "SELECT * FROM users LEFT JOIN paintings ON paintings.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        user = cls(results[0])
        for result in results:
            painting_data = {
                'id': result['paintings.id'],
                'title': result['title'],
                'description': result['description'],
                'price': result['price'],
                'user_id': result['user_id'],
            }
            user.paintings.append(painting(painting_data))
        return user

    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if user['password'] != user['confirm-password']:
            flash("Passwords do not match")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid