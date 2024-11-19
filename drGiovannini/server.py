from datetime import datetime

from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='/static')

current_year = datetime.now().year

@app.route('/')
@app.route('/<route_name>')
def home(route_name=None):
    if route_name is None:
        return render_template(
            template_name_or_list='welcome.html',
            current_year=current_year, # for keeping copyright up to date
            page_title='Dr Stefano Giovannini',
            meta_description='Dr Stefano Giovannini is an Italian native fluent in English and Mandarin Chinese. '
                             'He provides language-teaching, translation, Python-programming, and housing-related '
                             'services. He is the Vice President of the Pedone Association for '
                             'the Intercultural Exchange (pedone.eu).'
        )
    elif route_name.lower() == 'bio':
        return render_template(
            template_name_or_list='bio.html',
            current_year=current_year,
            page_title='Dr Stefano Giovannini\'s bio',
            meta_description='Dr Stefano Giovannini has a PhD in Digital Humanities, is fluent in English and Chinese, '
                             'is a skilled Python programmer, and is the Vice President of the Pedone Association for '
                             'the Intercultural Exchange (pedone.eu). He provides services related to language teaching,'
                             ' translation, Python programming, and housing in Lombardy.'
        )
    elif route_name.lower() == 'email':
        return render_template(
            template_name_or_list='email.html',
            current_year=current_year,
            page_title='Dr Stefano Giovannini\'s e-mail',
            meta_description='Dr Stefano Giovannini\'s e-mail for inquiries related to language teaching,'
                             ' translation, Python programming, and housing in Lombardy.'
        )
    elif route_name.lower() == 'pedone':
        return render_template(
            template_name_or_list='pedone.html',
            current_year=current_year,
            page_title='Dr Stefano Giovannini Vice President of Pedone Association',
            meta_description='Dr Stefano Giovannini is the Vice President of the Pedone Association for '
                             'the Intercultural Exchange (pedone.eu), whose mission is the promotion of Chinese art '
                             'among Westerners and Western art among Chinese.'
        )
    elif route_name.lower() == 'services':
        return render_template(
            template_name_or_list='services.html',
            current_year=current_year,
            page_title='Dr Stefano Giovannini\'s services',
            meta_description='Dr Stefano Giovannini provides services related to language teaching,'
                             ' translation, Python programming, and housing in Lombardy. This page lists the most '
                             'frequently requested among them.'
        )
    else:
        return render_template(
            template_name_or_list='404.html',
            current_year=current_year,
            page_title='Dr Stefano Giovannini - 404',
            meta_description='Dr Stefano Giovannini uses this page to notify the user that the requested route does not'
                             ' exist on drgiovannini.com.'
        )
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == '__main__':
    app.run(debug=False) # set to True in development, False when publishing on remote repositories and in production