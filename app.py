from flask import Flask
from flask import render_template, request
from search import SearchForm
from config import Config

from goat import getShoe

app = Flask(__name__)

app.config['DEBUG'] = True
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        smallestSize = request.form.get('smallSize')
        df = getShoe(request.form.get('searchQuery'))
        return render_template('post.html', sm=smallestSize, tables=[df.to_html(classes='data')], titles=df.columns.values)
    else:
        s = SearchForm()
        return render_template('get.html', search=s)

@app.route('/hello')
def hello():
    return 'Hello, World'