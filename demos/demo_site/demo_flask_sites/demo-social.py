from flask import Flask, render_template_string
from mypy_8tml import MyPy8TML

app = Flask(__name__)

# Define o cabeçalho da página
header = MyPy8TML()
header.div.in_class('header')\
    .h1['Minha Rede Social']()

# Define o menu da página
menu = MyPy8TML()
menu.div.in_class('menu')\
    .ul\
        .li\
            .a.in_href('#')['Início']()\
        .li\
            .a.in_href('#')['Perfil']()\
        .li\
            .a.in_href('#')['Amigos']()\
        .li\
            .a.in_href('#')['Configurações']()

# Define as postagens da página
posts = MyPy8TML()
posts.div.in_class('postagens')\
    .div.in_class('postagem')\
        .img.in_src('https://via.placeholder.com/150')\
        .div.in_class('conteudo')\
            .h2['Título da postagem']()\
            .p['Texto da postagem']()\
            .button.in_type('button')['Curtir']()\
            .button.in_type('button')['Comentar']()\
    .div.in_class('postagem')\
        .img.in_src('https://via.placeholder.com/150')\
        .div.in_class('conteudo')\
            .h2['Título da postagem']()\
            .p['Texto da postagem']()\
            .button.in_type('button')['Curtir']()\
            .button.in_type('button')['Comentar']()

# Define o rodapé da página
footer = MyPy8TML()
footer.div.in_class('footer')\
    .p['Copyright © 2023']()

# Define o template da página
template = MyPy8TML()

template.init_html('Minha Rede Social', 'pt')\
    [header]\
    [menu]\
    [posts]\
    [footer]()


@app.route('/')
def index():
    return render_template_string(template.generate())


app.run(debug=True)
