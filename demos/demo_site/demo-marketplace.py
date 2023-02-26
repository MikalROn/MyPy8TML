from flask import Flask, render_template_string
from mypy_8tml import MyPy8TML

app = Flask(__name__)

# Define o cabeçalho da página
header = MyPy8TML()
header.div.in_class('header')\
    .h1['Compre Produtos Usados']()

# Define o menu da página
menu = MyPy8TML()
menu.div.in_class('menu')\
    .ul\
        .li\
            .a.in_href('#')['Início']()\
        .li\
            .a.in_href('#')['Produtos']()\
        .li\
            .a.in_href('#')['Carrinho']()\
        .li\
            .a.in_href('#')['Minha Conta']()\
        .li\
            .a.in_href('#')['Sair']()

# Define a lista de produtos
products = MyPy8TML()
products.div.in_class('products')\
    .div.in_class('product')\
        .img.in_src('https://via.placeholder.com/150')\
        .div.in_class('content')\
            .h2['Produto 1']()\
            .p['Descrição do Produto 1']()\
            .p['Preço: R$ 50,00']()\
            .button.in_type('button')['Adicionar ao Carrinho']()\
    .div.in_class('product')\
        .img.in_src('https://via.placeholder.com/150')\
        .div.in_class('content')\
            .h2['Produto 2']()\
            .p['Descrição do Produto 2']()\
            .p['Preço: R$ 30,00']()\
            .button.in_type('button')['Adicionar ao Carrinho']()\
    .div.in_class('product')\
        .img.in_src('https://via.placeholder.com/150')\
        .div.in_class('content')\
            .h2['Produto 3']()\
            .p['Descrição do Produto 3']()\
            .p['Preço: R$ 20,00']()\
            .button.in_type('button')['Adicionar ao Carrinho']()

# Define o rodapé da página
footer = MyPy8TML()
footer.div.in_class('footer')\
    .p['Copyright © 2023']()

# Define o template da página
template = MyPy8TML()

template.init_html('Compre Produtos Usados', 'pt')\
    [header]\
    [menu]\
    [products]\
    [footer]()


@app.route('/')
def index():
    return render_template_string(template.generate())


app.run(debug=True)
