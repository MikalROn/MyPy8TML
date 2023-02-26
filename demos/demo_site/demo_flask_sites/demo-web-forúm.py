from flask import Flask, request, redirect
from mypy_8tml import MyPy8TML

app = Flask(__name__)

messages = []

# Criação do formulário
form = MyPy8TML().init_html('Forum Anônimo', 'pt-BR')
form.div.in_class('container')\
    .form.in_class('form').in_action('/send_message').in_method('POST')\
        .h1['Envie sua mensagem']()\
        .p['Nickname:'](-1).input.in_type('text').in_name('nickname')()\
        .p['Mensagem:'](-1).textarea.in_name('message')()\
        .button.in_type('submit')['Enviar']()

# Criação da página inicial com as mensagens já enviadas
@app.route('/')
def index():
    messages_list = MyPy8TML()
    messages_list.div.in_class('container')\
        .h1['Mensagens']()['<hr>']()

    for msg in messages:
        messages_list.div.in_class('card')\
            .div.in_class('card-body')\
            .h5.in_class('card-title')[msg['nickname']]()\
            .p.in_class('card-text')[msg['message']]()

    return form.generate() + messages_list.generate()

# Criação da rota para envio de novas mensagens
@app.route('/send_message', methods=['POST'])
def send_message():
    nickname = request.form.get('nickname')
    message = request.form.get('message')
    messages.append({'nickname': nickname, 'message': message})
    return redirect('/')

# Inicia o servidor local
app.run(debug=True)