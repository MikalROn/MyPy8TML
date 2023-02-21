from mypy_8tml import MyPy8TML
from flask import Flask

app = Flask(__name__)

index = MyPy8TML()

form2 = MyPy8TML()

index.import_style('style.css')

form2.import_style('style.css')

index = index\
    .div.in_class('login-page')\
        .div.in_class('form')\
            .form.in_class('register-form')\
                .input['type="text" placeholder="name"', 'in']()\
                .input['type="password" placeholder="password"', 'in']()\
                .input['type="text" placeholder="email address"', 'in']()\
                .button['create']()\
                .p.in_class('message')['Already registered? '].a.in_href('#')['Sign In'](3)\
            .form.in_class('login-form')\
                .input['type="text" placeholder="username"', 'in']()\
                .input['type="password" placeholder="password"', 'in']()\
                .button['login']()\
                .p.in_class('message')['Not registered? '].a.in_href('#')['Create an account']

form2 = form2 \
    .div.in_class('login-page') \
        .div.in_class('form') \
            .form.in_class('register-form') \
                .input['type="text" placeholder="name"', 'in']() \
                .input['type="password" placeholder="password"', 'in']() \
                .input['type="text" placeholder="email address"', 'in']() \
                .button['create']() \
                .p.in_class('message')['Already registered? '].a.in_href('#')['Sign In'](3) \
            .form.in_class('login-form') \
                .input['type="text" placeholder="username"', 'in']() \
                .input['type="password" placeholder="password"', 'in']() \
                .button['login']() \
                .p.in_class('message')['Not registered? '].a.in_href('#')['Create an account']

html = index.generete()

html2 = form2.generete()


@app.route('/')
def index():
    return html


@app.route('/1')
def form():
    return html2


app.run(debug=True)
