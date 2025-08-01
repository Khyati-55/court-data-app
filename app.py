from flask import Flask, render_template, request, redirect, flash
from scraper.court_scraper import fetch_case_data
from db.db import init_db, log_query

app = Flask(__name__)
app.secret_key = 'secret'  # You can replace this with an env variable
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        year = request.form['year']

        try:
            data = fetch_case_data(case_type, case_number, year)
            log_query(case_type, case_number, year, str(data))
            return render_template('index.html', data=data)
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect('/')

    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
