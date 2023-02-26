import io
import sys
from flask import Flask, render_template_string, request
from mypy_8tml import MyPy8TML


app = Flask(__name__)


head = MyPy8TML()

head.\
    link['rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.css"', 'in']()\
    .script.in_src('https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.js')()\
    .script.in_src('https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/mode/python/python.min.js')()


# Define o template da página
template = MyPy8TML().init_html('Executar código Python', 'pt', charset='latin-1', inhead=head.generate())

template.h1['Executar código python']()\
    .form.in_method('post')\
        .label.in_for('codigo')()\
        .textarea.in_id('code').in_class('python').in_name('codigo')['{{ codigo|safe }}'](-1).br(-1)\
        .input.in_type('submit').in_value('Executar')(2)\
    .h2['Saída:']()\
    ['<pre><code id="console">{{ saida|safe }}</code></pre>']()\
    .script['''
            var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
            mode: "python",
            lineNumbers: true,
            styleActiveLine: true,
            matchBrackets: true
            });
    '''](2)\
    .style['body{background-color:black;} h1, h2, pre{color:white;}']()


@app.route('/', methods=['GET', 'POST'])
def executar_codigo():
    codigo = request.form.get('codigo', '')
    saida = ''
    if codigo:
        # Captura a saída do código Python
        stdout = io.StringIO()
        sys.stdout = stdout
        exec(codigo)
        saida = stdout.getvalue()
        sys.stdout = sys.__stdout__
    return render_template_string(template.generate(), saida=saida, codigo=codigo)


if __name__ == '__main__':
    app.run(debug=True)
