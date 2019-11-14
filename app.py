import imdb
import json
import xmltodict
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.secret_key = 'secret'
bootstrap = Bootstrap(app)


ia = imdb.IMDb()


class SearchForm(FlaskForm):
    search = StringField('search')
    submit = SubmitField('Search')


@app.route('/movie/${id}')
def movie():
    pass


@app.route('/show/${id}')
def show():
    pass


@app.route('/search')
def search():
    args = request.args
    print(args)
    s = args['query']
    movies = []
    for entry in ia.search_movie(s):
        temp = xmltodict.parse(entry.asXML())
        movies.append(json.dumps(temp))
    #print(movies[0])
    return render_template('movies.html', movies=movies)


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
