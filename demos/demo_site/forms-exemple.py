from flask import Flask, render_template_string
from mypy_8tml import MyPy8TML

app = Flask(__name__)

register = MyPy8TML().init_html('Form', 'pt')

register.div.in_class('flex-box')\
        .form.in_class('form')\
            .h1[' Just a simple form']()\
            .p['e-mail :'](-1).input.in_type('email')()\
            .p['password :'](-1).input.in_type('password')()\
            .button.in_type('submit')['submit']()\

contato = MyPy8TML()

contato.div.in_class('flex-box')\
        .form.in_class('form')\
            .h1['Entre em contato conosco']()\
            .p['Nome completo:'](-1).input.in_type('text')()\
            .p['E-mail:'](-1).input.in_type('email')()\
            .p['Mensagem:'](-1).textarea.in_name('message')()\
            .button.in_type('submit')['Enviar']()

search = MyPy8TML()

search.div.in_class('flex-box')\
        .form.in_class('form')\
            .h1['Pesquise aqui']()\
            .p['Palavras-chave:'](-1).input.in_type('text')()\
            .p['Categoria:'](-1)\
                    .select.in_name('category')\
                        .option['Todas']()\
                        .option['Notícias']()\
                        .option['Esportes']()\
                        .option['Entretenimento'](2)\
            .button.in_type('submit')['Pesquisar']()

index = MyPy8TML().init_html('Menu', 'pt')

index.nav.in_class('menu')\
        .ul\
            .li\
                .a.in_href('/register').button['Registre-se'](3)\
            .li\
                .a.in_href('/contact').button['Contato'](3)\
            .li\
                .a.in_href('/search').button['Pesquisa'](3)\
            .li\
                .a.in_href('/about').button['Sobre'](3)\
            .li\
                .a.in_href('/products').button['Produtos'](3)\
            .li\
                .a.in_href('/team').button['Equipe'](3)

about = MyPy8TML().init_html('Sobre', 'pt')

about.div.in_class('container')\
        .h1['Sobre Nós']()\
        .p['Somos uma empresa dedicada a fornecer soluções tecnológicas inovadoras para nossos clientes.']()\
        .p['Entre em contato conosco para saber mais sobre nossos serviços.']()

products = MyPy8TML().init_html('Produtos', 'pt')

products.div.in_class('container')\
        .h1['Nossos Produtos']()\
        .ul\
            .li['Produto 1']()\
            .li['Produto 2']()\
            .li['Produto 3']()

team = MyPy8TML().init_html('Equipe', 'pt')

team.div.in_class('container')\
        .h1['Conheça Nossa Equipe']()\
        .ul\
            .li['João Silva - CEO']()\
            .li['Maria Santos - Gerente de Marketing']()\
            .li['Pedro Alves - Desenvolvedor Sênior']()


@app.route('/')
def index_page():
    return index.generate()


@app.route('/team')
def team_page():
    return team.generate()


@app.route('/products')
def products_page():
    return products.generate()


@app.route('/about')
def about_page():
    return about.generate()


@app.route('/register')
def cass_form():
    return register.generate()


@app.route('/contact')
def contact_form():
    return contato.generate()


@app.route('/search')
def search_form():
    return search.generate()


app.run(debug=True)
