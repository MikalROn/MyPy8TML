from flask import Flask, request, render_template, redirect
from templates_creation import generate_templates
app = Flask(__name__)


generate_templates()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data here
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Do something with the data, e.g. send an email
        return redirect('/')
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)