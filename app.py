from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask('my_app')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.POSTGRE_URI)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AdvertisementModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    head = db.Column(db.String)
    text = db.Column(db.String)
    date = db.Column(db.DateTime)
    owner = db.Column(db.String)


class AdvertisementView(MethodView):

    def get(self, advertisement_id):
        advertisement = AdvertisementModel.query.get(advertisement_id)
        if not advertisement:
            response = jsonify({'status': 'error', 'message': 'not found'})
            response.status_code = 404
            return response
        response = jsonify(
            {
                'id': advertisement.id,
                'head': advertisement.head,
                'text': advertisement.text,
                'date': advertisement.date,
                'owner': advertisement.owner
            }
        )
        return response

    def post(self):
        user_data = request.json
        new_advertisement = AdvertisementModel(**user_data)
        db.session.add(new_advertisement)
        db.session.commit()
        response = jsonify(
            {
                'id': new_advertisement.id,
                'head': new_advertisement.head,
                'text': new_advertisement.text,
                'date': new_advertisement.date,
                'owner': new_advertisement.owner
            }
        )
        return response

    def delete(self, advertisement_id):
        AdvertisementModel.query.filter(AdvertisementModel.id == advertisement_id).delete(
            synchronize_session='evaluate')
        db.session.commit()
        response = jsonify(
            {
                'advertisement_id': advertisement_id,
                'status': 'deleted'
            }
        )
        return response

    def patch(self, advertisement_id):
        user_data = request.json
        AdvertisementModel.query.filter(AdvertisementModel.id == advertisement_id).update(user_data)
        db.session.commit()
        response = jsonify(
            {
                'advertisement_id': advertisement_id,
                'status': 'updated'
            }
        )
        return response



app.add_url_rule('/advertisement/<advertisement_id>', view_func=AdvertisementView.as_view('get_advertisement'),
                 methods=['GET'])
app.add_url_rule('/advertisement/', view_func=AdvertisementView.as_view('create_advertisement'), methods=['POST'])
app.add_url_rule('/advertisement/<advertisement_id>', view_func=AdvertisementView.as_view('delete_advertisement'),
                 methods=['DELETE'])
app.add_url_rule('/advertisement/<advertisement_id>', view_func=AdvertisementView.as_view('update_advertisement'),
                 methods=['PATCH'])
app.run(host='0.0.0.0', port=8080)
