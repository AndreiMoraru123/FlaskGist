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
    files = gist['files']

    return render_template('gists.html', gist=gist, files=files)


@app.route('/file/<file_id>')
def file(file_id):
    api_url = f'https://api.github.com/gists/{file_id}'
    r = requests.get(api_url)
    gist = r.json()

    # Find the file with the specified file_id in the gist
    file = None
    for f in gist['files']:
        if f['id'] == file_id:
            file = f
            break

    if file:
        # Return the content of the file to the client
        return { 'content': file['content'] }
    else:
        # Return an error if the file was not found
        return { 'error': 'File not found' }, 404


if __name__ == '__main__':
    app.run(debug=True)
