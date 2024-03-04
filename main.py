from flask import Flask, make_response, request, session, render_template, redirect
from flask_login import LoginManager, login_user
from forms.login import LoginForm
from data.users import User
from data.news import News
from data import db_session, news_api
from flask_restful import Api
from data import news_resources


app = Flask(__name__)
api = Api(app)
# для списка объектов
api.add_resource(news_resources.NewsListResource, '/api/v2/news')
# для одного объекта
api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
