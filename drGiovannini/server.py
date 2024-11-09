from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

current_year = datetime.now().year

@app.route('/')
@app.route('/<route_name>')
def home(route_name=None):
    if route_name is None:
        return render_template(
            template_name_or_list='welcome.html',
            current_year=current_year # for keeping copyright up to date
        )
    elif route_name.lower() == 'bio':
        return render_template(
            template_name_or_list='bio.html',
            current_year=current_year
        )
    elif route_name.lower() == 'email':
        return render_template(
            template_name_or_list='email.html',
            current_year=current_year
        )
    elif route_name.lower() == 'pedone':
        return render_template(
            template_name_or_list='pedone.html',
            current_year=current_year
        )
    elif route_name.lower() == 'services':
        return render_template(
            template_name_or_list='services.html',
            current_year=current_year
        )
    else:
        return render_template(
            template_name_or_list='404.html',
            current_year=current_year
        )

if __name__ == '__main__':
    app.run(debug=False) # set to True in development, False when publishing on remote repositories and in production