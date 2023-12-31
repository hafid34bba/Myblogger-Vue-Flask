from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
import uuid
from models import Blogs

from db import db


def create_app(bd_url=None):
    # app = Flask(__name__, static_folder='dist')
    app = Flask(__name__)
    # CORS(app, resources={r"/api/*": {"origins": "http://4.232.9.93"}})
    # app.config['CORS_HEADERS'] = 'application/json'
    # CORS(app, resources={r"/*": {"origins": "http://4.232.9.93"}})
    CORS(app)
    app.config.from_object(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = bd_url or 'sqlite:///database.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)





    # BLOGS = [
    #     {"id" : uuid.uuid4().hex,
    #      "title" : "Blog 1",
    
    #      "resume" : "Data science is the art of discovring the hidden patterns...",
    #      "Contenu": "Data science is the art of discovring the hidden patterns in the data"
    #      },
    #      {"id" : uuid.uuid4().hex,
    #      "title" : "Blog 2",

    #      "resume" : "Data engineer has as role to prepare the infrastrcture for...",
    #      "Contenu": "Data engineer has as role to prepare the infrastrcture for data analysis and scientist"
    #              }
        

    # ]

    @app.route('/blogs', methods=['GET', 'OPTIONS'])

    def get_blogs():
        if request.method == 'OPTIONS':
            response = make_response()
            response.headers.add('Access-Control-Allow-Methods', 'POST')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            return response

        try: 
            blogs = Blogs.query.all()

            serialized_blogs = [{
                'id': blog.id,
                'title': blog.title,
                'Contenu': blog.Contenu
            } for blog in blogs]

            return jsonify(
                {
                    "status" : "success",
                    "blogs" : serialized_blogs
                }
            ), 200
        except Exception as e:
            response = {
                "status": "error",
                "message": "An error occurred while fetching blogs",
                "error": str(e)
            }
            return jsonify(response), 500


    @app.route('/create_blog', methods=['POST', 'OPTIONS'])
    def add_blog():

        if request.method == 'OPTIONS':
            response = make_response()
            response.headers.add('Access-Control-Allow-Methods', 'POST')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            return response

        response_object = {'status': 'success'}
        if request.method == "POST":
            post_data = request.get_json()

            # resume = " ".join(post_data['Contenu'].split(" ")[:10]) + '...'

            

            blog = Blogs(title = post_data['title'],
                        Contenu = post_data['Contenu'])

            # BLOGS.append( { 'id' : uuid.uuid4().hex, "resume" : resume,  **post_data})

            db.session.add(blog)
            db.session.commit()

            response_object['message'] = 'Blog Added'

            return jsonify(response_object), 200
        else : 
            return {
                "error": "Method not allowed"
            }, 405

    return app



def create_dep_app() : 
    app = create_app()
    with app.app_context():
        db.create_all()
    return app

if __name__ == '__main__':
    
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)