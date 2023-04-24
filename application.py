from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

EXTERNAL_SEARCH_URL = 'https://google.com/search'

@app.route('/')
def index():
    return redirect(EXTERNAL_SEARCH_URL)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        return redirect(f'{EXTERNAL_SEARCH_URL}?q={query}')
    else:
        return render_template_string('''
            <!DOCTYPE html>
            <html>
              <head>
                <title>ShadowSurf</title>
                <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
              </head>
              <body>
                <div class="container">
                  <h1>ShadowSurf</h1>
                  <form action="{{ url_for('search') }}" method="get">
                    <input type="text" name="q" placeholder="Search...">
                    <button type="submit">Go</button>
                  </form>
                </div>
              </body>
            </html>
        ''')

if __name__ == '__main__':
    app.run()
