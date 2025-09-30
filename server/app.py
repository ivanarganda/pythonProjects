from flask import Flask, request, jsonify
from markupsafe import escape

import sqlite3 as sql
from conf.DB import Database
import os

from dotenv import load_dotenv
from helpers.utils import get_queries
from conf.conn import init_connection, init_tables

load_dotenv()

user_admin = os.getenv("ADMIN_USER")
password_admin = os.getenv("PASSWORD_USER")

db = Database()

app = Flask(__name__)

def handle_server():

    if init_connection( db ) == False: raise Exception("🤔 Something went wrong in the server!!")

def parse_json_response( message , status = 200 ):

    return jsonify(
            message=message,
            status=status
        )


# Define routes outside of __main__ block
@app.route("/roles", methods=["GET"])
def get_roles():

    try:

        handle_server()

        db.execute_query(
            """ 
                SELECT * from roles
            """
        )

        result = db.fetch_all()

        return parse_json_response( result )

    except Exception as e:

        return parse_json_response( str(e) , 400 )

@app.route("/users", methods=["GET"])
def get_users():

    try:

        handle_server()

        db.execute_query(
            """ 
                SELECT * from users
            """
        )

        result = db.fetch_all()

        return parse_json_response( result )

    except Exception as e:
        
        return parse_json_response( str(e) , 400 )

if __name__ == "__main__":
    try:
        # initialize DB before running server
        handle_server()

        if init_tables( db ) == False: raise Exception("❌ unable intializing tables in database")

        app.run(host="0.0.0.0", port=5000, debug=True)
    
    except Exception as e:

        print(e)