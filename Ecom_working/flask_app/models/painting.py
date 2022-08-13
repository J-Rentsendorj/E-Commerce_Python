from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re


DATABASE = 'paintings'

class Painting:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.user_id = data['user_id']

#! CREATE
#! class method to add a painting to the DB 
    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO paintings (title, description, price, user_id) VALUES ( %(title)s, %(description)s, %(price)s, %(user_id)s );"
        return connectToMySQL(DATABASE).query_db( query, data )
        #! the return stmt returns the id as an int of the painting created

#! READ
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT paintings.*, users.first_name FROM paintings LEFT JOIN users ON users.id = paintings.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        paintings = []
        for painting in results: 
            paintings.append( cls(painting) )
        print(paintings)
        return paintings

#! READ
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM paintings WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

#! UPDATE
    @classmethod
    def update(cls, data:dict) -> object:
        query = 'UPDATE paintings SET title=%(title)s, description=%(description)s, price=%(price)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! DELETE
    @classmethod
    def destroy(cls, data:dict) -> object:
        query = 'DELETE FROM paintings WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

#! VALIDATION
    @staticmethod
    def validate_painting(painting:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(painting['title']) < 2:
            flash("Title must be at least 2 characters.")
            is_valid = False
        if len(painting['description']) < 10:
            flash("Description must be at least 10 characters.")
            is_valid = False
        if  painting['price'] == 0:
            flash("Price should be greater than 0.")
            is_valid = False
        return is_valid