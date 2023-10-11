from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
from models import Blogs

from db import db


def create_app(bd_url=None):
    app = Flask(__name__)
    CORS(app, ressources={r"/*":{'originis':"*"}})
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

    @app.route('/blogs', methods=['GET'])
    def get_blogs():

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


    @app.route('/create_blog', methods=["POST"])

    def add_blog():
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

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)