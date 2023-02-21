from mypy8tml.template import MyPy8TML
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
        .style[
            '''
            body{
                pading: 0
            }
            .cabeçalho{
            
            }
            .titulo{
                font-size: 1.75rem;
                line-height: 2.25rem;
                font-family: ReithSerif, Helvetica, Arial, sans-serif;
                font-weight: 500;
                font-style: normal;
                color: rgb(20, 20, 20);
                display: block;
                margin: 0px;
                padding: 2rem 0px;
                overflow-wrap: anywhere;
                }
    
            img {
            pading: 0;
            height: 100%;
            background-color: rgb(300, 300, 300);
            width: 200px;
            }
            header {
            pading: 0;
            background-color: rgb(184, 0, 0);
            height: 100px;
            width: 100%;
            position: relative;
        }''']()


print(html.generete())


@app.route('/')
def index():
    return html.generete()


app.run(debug=True)