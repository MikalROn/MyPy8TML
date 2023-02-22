from flask import Flask
from mypy_8tml import MyPy8TML

app = Flask(__name__)

form = MyPy8TML()

form.div.in_type('flex-box')\
        .form.in_class('form')\
            .h1[' Just a simple form']()\
            .div.p['e-mail :'](-1).input.in_type('email')(2)\
            .div.p['password :'](-1).input.in_type('password')(2)\
            .button.in_type('submit')['submit']()\



@app.route('/')
def cass_form():
    return form.generete()


app.run(debug=True)
