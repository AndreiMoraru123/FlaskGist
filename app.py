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
    files = []
    for filename, file in gist['files'].items():
        try:
            # Make a request to the file's raw URL to get its content
            r = requests.get(file['raw_url'])
            content = r.text
            # Add the content to the file object
            file['content'] = content
        except Exception as e:
            # Set the content to an error message if the request fails
            file['content'] = f'Error loading file: {e}'
            print(f'Error loading file: {e}')
        files.append(file)

    return render_template('gists.html', gist=gist, files=files)


if __name__ == '__main__':
    app.run(debug=True)
