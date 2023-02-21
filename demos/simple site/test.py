from mypy_8tml import MyPy8TML
from flask import Flask

app = Flask(__name__)

index = MyPy8TML()


bbc_logo = 'https://upload.wikimedia.org/wikipedia/commons/4/41/BBC_Logo_2021.svg'



html = index\
        .init_html('daniel', 'pt')\
        .header\
            .div['class="cabeçalho"', 'in']\
                .img[f'src="{bbc_logo}"', 'in']()\
                .h1['class="titulo"', 'in'][' News '](2)\

html.import_style('style.css')


print(html.generete())


@app.route('/')
def index():
    return html.generete()


app.run(debug=True)