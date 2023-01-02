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

    gist_forks = {}
    for gist in gists:
        try:
            forks_url = gist['forks_url']
            r = requests.get(forks_url)
            gist_forks[gist['id']] = r.json()
        except TypeError:  # this is in case the API limit is reached
            continue

    return render_template('search_results.html', gists=gists, gist_forks=gist_forks)


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

    logoMap = {
        'js': {'name': 'JavaScript', 'color': '#f7df1e'},
        'py': {'name': 'Python', 'color': '#3572A5'},
        'html': {'name': 'HTML', 'color': '#e34c26'},
        'css': {'name': 'CSS', 'color': '#563d7c'},
        'java': {'name': 'Java', 'color': '#b07219'},
        'c': {'name': 'C', 'color': '#555'},
        'cs': {'name': 'C#', 'color': '#178600'},
        'cpp': {'name': 'C++', 'color': '#f34b7d'},
        'rb': {'name': 'Ruby', 'color': '#701516'},
        'go': {'name': 'Go', 'color': '#375eab'},
        'swift': {'name': 'Swift', 'color': '#ffac45'},
        'sh': {'name': 'Shell', 'color': '#89e051'},
        'rs': {'name': 'Rust', 'color': '#dea584'},
        'hs': {'name': 'Haskell', 'color': '#5e5086'},
        'lua': {'name': 'Lua', 'color': '#000080'},
        'erl': {'name': 'Erlang', 'color': '#b83998'},
        'ex': {'name': 'Elixir', 'color': '#6e4a7e'},
        'ps1': {'name': 'PowerShell', 'color': '#012456'}
    }

    return render_template('gists.html', gist=gist, files=files, logoMap=logoMap)


if __name__ == '__main__':
    app.run(debug=True)
