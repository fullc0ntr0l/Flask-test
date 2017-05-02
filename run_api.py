from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class NewImage(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('image', type=unicode, required=True)

    def post(self):
        args = self.parser.parse_args()
        image = args.get('image')
        base64_image = ImageModel(image)
        db.session.add(base64_image)
        db.session.commit()
        return {'id': base64_image.id}


class GetImage(Resource):
    def get(self, image_id):
        base64_image = ImageModel.query.get(image_id)
        if base64_image is None:
            return {'error': 'Image not found'}, 404
        return base64_image.serialize


class ImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base64 = db.Column(db.Text)

    def __init__(self, base64):
        self.base64 = base64

    @property
    def serialize(self):
        return {
            'image': self.base64
        }

db.create_all()


api.add_resource(NewImage, '/image')
api.add_resource(GetImage, '/image/<int:image_id>')


if __name__ == '__main__':
    app.run(debug=True)
