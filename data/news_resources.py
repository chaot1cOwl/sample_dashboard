from flask import jsonify
from flask_restful import Resource, abort

from . import db_session
from .news import News
from .reqparse import parser


class NewsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        db = db_session.create_session()
        news = db.query(News).get(news_id)
        return jsonify({'news': news.to_dict(only=('title', 'content', 'user_id'))})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        db = db_session.create_session()
        news = db.query(News).get(news_id)
        db.delete(news)
        db.commit()
        return jsonify({'success': 'OK'})


class NewsListResource(Resource):
    def get(self):
        db = db_session.create_session()
        news = db.query(News).all()
        return jsonify(
            {'news': [item.to_dict(only=('title', 'content', 'user_id')) for item in news]})

    def post(self):
        args = parser.parse_args()
        db = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id']
        )
        db.add(news)
        db.commit()
        return jsonify({'success': 'OK'})


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    print(news_id)
    news = session.query(News).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")
