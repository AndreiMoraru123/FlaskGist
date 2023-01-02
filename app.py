from flask import Flask, render_template, request, jsonify
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


import requests

@app.route('/file/<file_id>')
def file(file_id):
    # Send a request to the API to get the metadata for the Gist
    api_url = f'https://api.github.com/gists/{file_id}'
    r = requests.get(api_url)
    gist = r.json()
    # Find the file object in the Gist with the matching file_id
    file_obj = None
    for file in gist['files']:
        if file['id'] == file_id:
            file_obj = file
            break

    # If a file object was found, send a request to the URL of the file to get its content
    if file_obj:
        r = requests.get(file_obj['raw_url'])
        content = r.text
    else:
        content = 'Error: file not found'

    # Return the content as a JSON object
    return jsonify({'content': content})



if __name__ == '__main__':
    app.run(debug=True)
