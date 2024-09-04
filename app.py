from flask import Flask, render_template
import json

app = Flask(__name__)


# Load site structure from JSON file
def load_site_structure():
    with open('site_structure.json') as f:
        return json.load(f)


@app.route('/')
@app.route('/<page_name>')
def render_page(page_name="index"):
    site_structure = load_site_structure()

    # Find the page details from the JSON
    for page in site_structure['pages']:
        if page['name'] == page_name:
            return render_template('dynamic_page.html', page=page)

    return "Page not found", 404


@app.route('/sitemap')
def sitemap():
    site_structure = load_site_structure()

    pages = site_structure['pages']
    pages_by_target = {}

    # Create a dictionary mapping page targets to page information and buttons
    for page in pages:
        pages_by_target[page['name']] = page

    return render_template('sitemap.html', pages=pages, pages_by_target=pages_by_target)



if __name__ == '__main__':
    app.run(debug=True)
