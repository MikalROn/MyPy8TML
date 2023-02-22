from flask import Flask
from mypy_8tml import MyPy8TML

app = Flask(__name__)

form = MyPy8TML().init_html('Form', 'pt')

form.div.in_class('flex-box')\
        .form.in_class('form')\
            .h1[' Just a simple form']()\
            .p['e-mail :'](-1).input.in_type('email')()\
            .p['password :'](-1).input.in_type('password')()\
            .button.in_type('submit')['submit']()\

html = form >> 'templates/index'


@app.route('/')
def cass_form():
    return form.generete()


app.run(debug=True)
