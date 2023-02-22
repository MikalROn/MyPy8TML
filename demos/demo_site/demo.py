from flask import Flask
from mypy_8tml import MyPy8TML

app = Flask(__name__)

# Página inicial
index = MyPy8TML().init_html('Página Inicial', 'pt')

index.div.in_class('container py-5')\
        .h1['Meu Site de Demonstração']()\
        .p['Bem-vindo ao meu site de demonstração! Aqui você encontrará algumas páginas simples que mostram o uso do Flask e do MyPy8TML para criar páginas da web.']()

# Sobre
about = MyPy8TML().init_html('Sobre', 'pt')

about.div.in_class('container py-5')\
        .h1['Sobre']()\
        .p['Meu nome é ChatGPT e eu criei este site de demonstração para mostrar como criar páginas da web com o Flask e o MyPy8TML.']()

# Contato
contact = MyPy8TML().init_html('Contato', 'pt')

contact.div.in_class('container py-5')\
        .h1['Contato']()\
        .form.in_class('form')\
            .div.in_class('mb-3')\
                .label.in_for('name')['Nome']()\
                .input.in_for('text').in_class('form-control')()\
            .div.in_class('mb-3')\
                .label.in_for('email')['Endereço de e-mail']()\
                .input.in_for('email').in_class('form-control')()\
            .div.in_class('mb-3')\
                .label.in_for('message')['Mensagem']()\
                .textarea.in_name('message').in_class('form-control').in_rows(5)()\
            .button.in_type('submit').in_class('btn btn-primary')['Enviar']()

# Rodapé
footer = MyPy8TML()

footer.footer.in_class('footer mt-auto py-3 bg-light')\
        .div.in_class('container text-center')\
            .span['Criado por ChatGPT © 2023']()

# Rotas
@app.route('/')
def index_page():
    return index.generate()


@app.route('/about')
def about_page():
    return about.generate()


@app.route('/contact')
def contact_page():
    return contact.generate()


@app.route('/favicon.ico')
def favicon():
    return ''


app.run(debug=True)
