from flask import Flask
from mypy_8tml import MyPy8TML

app = Flask(__name__)

page = MyPy8TML().init_html('Minha Página', 'pt')

# Cabeçalho
page.header\
    .nav\
        .ul.in_class('menu')\
            .li\
                .a.in_href('#home')['Home']()\
            .li\
                .a.in_href('#sobre')['Sobre']()\
            .li\
                .a.in_href('#contato')['Contato']()\
        .button.in_class('menu-toggle')['Menu']()\
    .div.in_class('hero')\
        .h1['Minha Página']()\
        .p['Bem-vindo à minha página criada com MyPy8TML!']()

# Seção Sobre
page.section.in_id('sobre')\
    .div.in_class('container')\
        .h2['Sobre']()\
        .p['Esta página foi criada com MyPy8TML, uma biblioteca Python para criar HTML de maneira simples e elegante.']\
        .p['MyPy8TML permite criar estruturas HTML complexas com facilidade, usando uma sintaxe '\
           'intuitiva baseada em objetos.(não foi eu quem disse isso foi o chatgtp)']()


# Seção Serviços
page.section.in_id('servicos')\
    .div.in_class('container')\
        .h2['Serviços']()\
        .ul\
            .li['Web design']()\
            .li['Desenvolvimento web']()\
            .li['SEO']()\
            .li['Marketing digital']()\
        .p['Oferecemos serviços de alta qualidade e com preços competitivos.']()

# Seção Portfólio
page.section.in_id('portfolio')\
    .div.in_class('container')\
        .h2['Portfólio']()\
        .div.in_class('grid')\
            .div.in_class('grid-item')\
                .a.in_href('#')['Projeto 1']()\
            .div.in_class('grid-item')\
                .a.in_href('#')['Projeto 2']()\
            .div.in_class('grid-item')\
                .a.in_href('#')['Projeto 3']()\
            .div.in_class('grid-item')\
                .a.in_href('#')['Projeto 4']()\
            .div.in_class('grid-item')\
                .a.in_href('#')['Projeto 5']()\
            .div.in_class('grid-item')\
                .a.in_href('#')['Projeto 6']()()

# Seção Contato
page.section.in_id('contato')\
    .div.in_class('container')\
        .h2['Contato']()\
        .form\
            .label.in_for('nome')['Nome:']\
            .input.in_type('text').in_name('nome')()\
            .label.in_for('email')['E-mail:']\
            .input.in_type('email').in_name('email')()\
            .label.in_for('mensagem')['Mensagem:']\
            .textarea.in_name('mensagem')()\
            .button.in_type('submit')['Enviar']()

# Rodapé
page.footer\
    .div.in_class('container')\
        .p['Copyright © 2023']()


@app.route('/')
def home():
    return page.generate()


app.run(debug=True)
