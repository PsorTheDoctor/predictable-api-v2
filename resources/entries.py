from flask_restful import Resource, abort, fields, marshal_with

from models.entry import EntryModel
from db import db_session
from utils.google_news import *

resource_fields = {
    'id': fields.Integer,
    'header': fields.String,
    'publisher': fields.String,
    'content': fields.String,
    'link': fields.String,
    'date': fields.String,
    'img': fields.String
}


class Entry(Resource):
    @marshal_with(resource_fields)
    def get(self, entry_id):
        response = EntryModel.query.filter_by(id=entry_id).first()
        if not response:
            abort(404, message="Entry {} doesn't exist.".format(entry_id))
        return response


class EntryList(Resource):
    @marshal_with(resource_fields)
    def get(self, qty):
        # Firstly, delete old entries
        while EntryModel.query.first():
            entry = EntryModel.query.first()
            db_session.delete(entry)
            db_session.commit()

        # Create some new entries for every method call
        for idx in range(qty):
            header = get_header(idx)
            publisher = get_publisher(idx)
            content = get_content(idx)
            link = get_link(idx)
            n_days_ago = get_num_days_ago(idx)
            img = get_base64_img()
            entry = EntryModel(header, publisher, content, link, n_days_ago, img)
            db_session.add(entry)
            db_session.commit()

        return EntryModel.query.limit(qty).all()
