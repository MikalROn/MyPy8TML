import pandas as pd

df = pd.read_csv('data4scripts/jinja.csv', sep=';')
fd = pd.read_csv('data4scripts/elementos_html.csv')

for tag in fd.itertuples():
    stag = tag[2].replace('<', '').replace('>', '')
    if tag[3] != 'Sim':
        expected = f'"<{stag}></{stag}>"'
    else:
        expected = f'"<{stag}>"'
    print(
        f'def test_{stag}(self):\n'
        f'  html = MyPy8TML()\n'
        f'  {stag} = html.{stag}.generate()\n'
        f'  assert {stag} == {expected}\n'
    )


comando_desc = [
    ("expressao", "Renderiza uma expressão como texto"),
    ("comando", "Executa um comando, como um loop ou uma condicional"),
    ("comentario", "Adiciona um comentário que é ignorado pelo Jinja"),
    ("if", "Inicia uma estrutura condicional"),
    ("elif", "Adiciona uma condição alternativa a um bloco if"),
    ("else", "Adiciona um bloco de código que é executado se a expressão do bloco if ou elif não for verdadeira"),
    ("endif", "Encerra um bloco if"),
    ("for", "Inicia um loop que itera sobre uma lista"),
    ("endfor", "Encerra um loop"),
    ("set", "Define uma variável no escopo atual"),
    ("block", "Inicia um bloco de conteúdo nomeado que pode ser estendido em outro template"),
    ("endblock", "Encerra um bloco"),
    ("extends", "Indica que o template atual estende um template pai e pode substituir os blocos definidos pelo template pai"),
    ("include", "Inclui um template em outro"),
    ("macro", "Define uma macro reutilizável"),
    ("endmacro", "Encerra uma macro"),
    ("filtro", "Renderiza uma expressão após aplicar um filtro"),
    ("filtro_arg", "Renderiza uma expressão após aplicar um filtro com argumentos"),
    ("filtro_seq", "Renderiza uma expressão após aplicar dois filtros em sequência"),
    ("set_filtro", "Define uma variável após aplicar um filtro a uma expressão"),
    ("include_var", "Inclui um template e define valores para as variáveis no momento da inclusão"),
    ("if_defined", "Verifica se uma variável está definida"),
    ("if_not_defined", "Verifica se uma variável não está definida"),
    ("if_none", "Verifica se uma variável é nula"),
    ("if_not_none", "Verifica se uma variável não é nula"),
    ("if_iterable", "Verifica se uma variável é iterável"),
    ("if_not_iterable", "Verifica se uma variável não é iterável")
]

comando_desc = [x[0] for x in comando_desc]

df = df.iloc[:27]
df['name'] = comando_desc

css = ['class,id,style,accesskey,tabindex,title,lang',
       'class,id,style,accesskey,tabindex,title',
       'class,id,style,accesskey,tabindex,title,bgcolor',
       'class,id,style,accesskey,tabindex,title,href,target,src,alt,width,height',
       'class,id,style,accesskey,tabindex,title,border,cellpadding,cellspacing',
       'class,id,style,accesskey,tabindex,title,colspan,rowspan,action,method,type,name,value',
       'class,id,style,accesskey,tabindex,title,name,rows,cols']
data = [
    string.split(',')
    for string in css
]
lista = []
for x in data:
    for y in x:
        lista.append(y)

atributos = ['alt', 'method', 'type', 'title',
             'bgcolor', 'src', 'width', 'colspan',
             'cols', 'rows', 'accesskey', 'border',
             'class', 'action', 'rowspan', 'value',
             'lang', 'style', 'cellpadding', 'height',
             'cellspacing', 'target', 'id', 'tabindex',
             'name', 'href']

'''for item in atributos:
    """    print(
        f'def in_{item}(self, value: str):\n' +
        "  self.in_content(f'" + item + '=' + '"{value}"' + "')\n" +
        f'  return self'
    )"""'''


'''for item in df.itertuples():
    print(
        f'def jnj_{item[3]}(self, expretion):\n'
        f'  self.content("{item[1]}")\n'
        f'  return self'
    )'''


