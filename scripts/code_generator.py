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
print(set(lista))

atributos = ['alt', 'method', 'type', 'title',
             'bgcolor', 'src', 'width', 'colspan',
             'cols', 'rows', 'accesskey', 'border',
             'class', 'action', 'rowspan', 'value',
             'lang', 'style', 'cellpadding', 'height',
             'cellspacing', 'target', 'id', 'tabindex',
             'name', 'href']

for item in atributos:
    print(
        f'def in_{item}(self, value: str):\n' +
        "  self.in_content(f'" + item + '=' + '"{value}"' + "')\n" +
        f'  return self'
    )





