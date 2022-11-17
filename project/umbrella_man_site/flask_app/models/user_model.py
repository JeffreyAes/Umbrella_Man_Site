import re
from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import DATABASE
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False

        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False

        return cls(results[0])

    @staticmethod
    def validator(data):
        is_valid = True
        # set true by default, set it to false if conditions aren't met
        if len(data['first_name']) == 0:
            flash("first name is required", 'reg')
            is_valid = False
        elif len(data['first_name']) < 2:
            flash("first name must be at least 2 characters long", 'reg')
            is_valid = False
        if len(data['last_name']) == 0:
            flash("last name is required", 'reg')
            is_valid = False
        elif len(data['last_name']) < 2:
            flash("last name must be at least 2 characters long", 'reg')
            is_valid = False
        if len(data['email']) < 1:
            flash('email is required', 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("invalid email", 'reg')
        else:
            user_data = {
                'email': data['email']
            }
            potential_user = User.get_by_email(user_data)
            if potential_user:
                flash('email already taken!', 'reg')
                is_valid = False

        if len(data['password']) < 8:
            flash("password must be 8 characters long", 'reg')
            is_valid = False
        elif not data['password'] == data['confirm_password']:
            flash("passwords must be the same", 'reg')
            is_valid = False
        return is_valid
