from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           image=popular_df['Image-URL-M'].to_list(),
                           book_name=popular_df['Book-Title'].to_list(),
                           author=popular_df['Book-Author'].to_list(),
                           votes=popular_df['num-ratings'].to_list(),
                           ratings=popular_df['avg_rating'].to_list()
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')

    ind = np.where(pt.index == user_input)[0][0]

    return render_template('recommend.html', data=ind)


if __name__ == '__main__':
    app.run(debug=True)
