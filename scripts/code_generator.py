import pandas as pd

df = pd.read_csv('data4scripts/jinja.csv', sep=';')

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

for item in atributos:
    """    print(
        f'def in_{item}(self, value: str):\n' +
        "  self.in_content(f'" + item + '=' + '"{value}"' + "')\n" +
        f'  return self'
    )"""

print(df)

for item in df.itertuples():
    print(
        f'def jnj_{item[3]}(self, expretion):\n'
        f'  self.content("{item[1]}")\n'
        f'  return self'
    )


def jnj_expretion(self, expretion):
  self.content("{{ " + expretion + " }}")
  return self

def jnj_comand(self, comand):
  self.content("{% " + comand + " %}")
  return self

def jnj_coment(self, coment):
  self.content("{# " + coment + " #}")
  return self

def jnj_if(self, expretion):
  self.content("{% if " + expretion + "%}")
  return self

def jnj_elif(self, expretion):
  self.content("{% elif " + expretion + " %}")
  return self

def jnj_else(self):
  self.content("{% else %}")
  return self

def jnj_endif(self):
  self.content("{% endif %}")
  return self

def jnj_block(self, name:str):
    self.content("{%" + name + "%}")
    return self

def jnj_endblock(self):
    self.content("{% endblock %}")
    return self

def jnj_extends_temp(self, template: str):
    self.content("{% extends " + template + " %}")
    return self

def jnj_include_temp(self, template: str):
    self.content("{% include " + template + " %}")
    return self

