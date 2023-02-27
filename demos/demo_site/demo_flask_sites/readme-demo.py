from flask import Flask, render_template_string
from mypy_8tml import MyPy8TML

app = Flask(__name__)

register = MyPy8TML().init_html('Form', 'pt')

register.div.in_class('flex-box')\
        .form.in_class('form')\
            .h1[' Just a simple form']()\
            .p['e-mail :'](-1).input.in_type('email')()\
            .p['password :'](-1).input.in_type('password')()\
            .button.in_type('submit')['submit']()


@app.route('/')
def index():
    return render_template_string(register.generate())

app.run(debug=True)