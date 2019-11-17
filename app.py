import imdb
import json
import xmltodict
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_paginate import Pagination, get_page_parameter
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.secret_key = 'secret'
bootstrap = Bootstrap(app)

ia = imdb.IMDb()
PER_PAGE = 4


class SearchForm(FlaskForm):
    search = StringField('search')
    submit = SubmitField('Search')


def searchIMDB(s, movie=True):
    for entry in ia.search_movie(s):
        temp = xmltodict.parse(entry.asXML())
        temp = json.loads(json.dumps(temp))
        if movie == True and temp['movie']['kind'] == 'movie':
            return temp
        elif movie == False and temp['movie']['kind'] == 'tv series':
            return temp


@app.route('/movie/<id>')
def movie(id):
    return searchIMDB(id, movie=True)


@app.route('/show/<id>')
def show(id):
    return searchIMDB(id, movie=False)


@app.route('/search')
def search():
    s = request.args['query']

    search_check = False
    q = request.args.get('q')
    if q:
        search_check = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    offset = (page - 1) * PER_PAGE

    movies = []
    imdb_search = ia.search_movie(s)
    for entry in imdb_search[offset:offset+PER_PAGE]:
        temp = xmltodict.parse(entry.asXML())
        movies.append(json.loads(json.dumps(temp)))

    pagination = Pagination(page=page,
                            offset=offset,
                            per_page=PER_PAGE,
                            total=len(imdb_search),
                            search=search_check,
                            css_framework='bootstrap3',
                            record_name='movies')

    return render_template('movies.html',
                           movies=movies,
                           pagination=pagination)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        q = request.form['search']
        print(q)
        return redirect('/search?query={}'.format(q))
    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run()
