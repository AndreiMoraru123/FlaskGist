from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    username = request.form['username']
    api_url = f'https://api.github.com/users/{username}/gists'
    r = requests.get(api_url)
    gists = r.json()

    # Process the gists data and extract the necessary information

    return render_template('search_results.html', gists=gists)

@app.route('/gist/<gist_id>')
def gist(gist_id):
    api_url = f'https://api.github.com/gists/{gist_id}'
    r = requests.get(api_url)
    gist = r.json()

    # Process the gist data and extract the necessary information

    return render_template('gists.html', gist=gist)


if __name__ == '__main__':
    app.run(debug=True)
