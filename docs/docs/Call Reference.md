# Methods

<dt><a name="MyPy8TML-init_html"><strong>init_html</strong></a>(self, title: str, lang: str, charset='UTF-8', inhead: str = '')</dt><p>Generates&nbsp;the&nbsp;stat&nbsp;of&nbsp;a&nbsp;html&nbsp;code&nbsp;until&nbsp;the&nbsp;body</p>

````html
<!DOCTYPE html>
<html lang=":param lang:">
<head>
    :param inhead:
    <meta charset=":param charset:">
    <title>:param title:</title>
</head>
<body> {UNTIL HERE}
````

<table>
    <tr>
        <td>title</td>
        <td>title&nbsp;of&nbsp;your&nbsp;html&nbsp;page</td>
    </tr>
    <tr>
        <td>lang</td>
        <td>lang&nbsp;of&nbsp;html</td>
    </tr>
    <tr>
        <td>charset</td>
        <td>lcharset&nbsp;of&nbsp;html</td>
    </tr>
    <tr>
        <td>inhead</td>
        <td>puts&nbsp;content&nbsp;un&nbsp;head</td>
    </tr>
    <tr>
        <td>return</td>
        <td>self</td>
    </tr>
</table>

<dl><dt><a name="MyPy8TML-set_filename"><strong>set_filename</strong></a>(self, name: str)</dt><dd>Set&nbsp;the&nbsp;name&nbsp;of&nbsp;output&nbsp;file</dd></dl>

<dt><a name="MyPy8TML-simple_down"><strong>simple_down</strong></a>(self, times: int = 1)</dt><p>This&nbsp;method&nbsp;allows&nbsp;to&nbsp;jump&nbsp;for&nbsp;next&nbsp;line</p>

<table>
    <tr>
        <td>times</td>
        <td>Number&nbsp;of&nbsp;tags&nbsp;that&nbsp;you&nbsp;want&nbsp;to&nbsp;go&nbsp;down&nbsp;in&nbsp;a&nbsp;code if&nbsp;negative&nbsp;close&nbsp;tag&nbsp;inline</td>
    </tr>
    <tr>
        <td>return</td>
        <td> self </td>
    </tr>
</table>

<dl><dt><a name="MyPy8TML-to_html"><strong>to_html</strong></a>(self, name: str, path: str = '') -&gt; None</dt><p>Export&nbsp;to&nbsp;Html</p>

<table>
    <tr>
        <td>name</td>
        <td>name&nbsp;of&nbsp;html&nbsp;code&nbsp;with&nbsp;sufix</td>
    </tr>
    <tr>
        <td>path</td>
        <td>path&nbsp;to&nbsp;put&nbsp;code&nbsp;with&nbsp;slash&nbsp;bar</td>
    </tr>
    <tr>
        <td>return</td>
        <td> None </td>
    </tr>
</table>

<a name="MyPy8TML-content"><strong>content</strong></a>(self, content: str)<p>content&nbsp;to&nbsp;main&nbsp;html&nbsp;code</p>

<dt><a name="MyPy8TML-downline"><strong>downline</strong></a>(self, times: int = 1)</dt>This&nbsp;method&nbsp;allows&nbsp;to&nbsp;close&nbsp;a&nbsp;tag<br>

<table>
    <tr>
        <td>times</td>
        <td>Number&nbsp;of&nbsp;tags&nbsp;that&nbsp;you&nbsp;want&nbsp;to&nbsp;go&nbsp;down&nbsp;in&nbsp;a&nbsp;code</td>
    </tr>
    <tr>
        <td>return</td>
        <td>self</td>
    </tr>
</table>

<dt><a name="MyPy8TML-generate"><strong>generate</strong></a>(self) -&gt; str<dd><tt>This&nbsp;method&nbsp;generetes&nbsp;the&nbsp;html&nbsp;final&nbsp;code.</tt></dd></dl>

<dt><a name="MyPy8TML-import_html"><strong>import_html</strong></a>(self, style_path, charset='UTF-8') -&gt; None</dt><p>Import html code from file code</p>

<table>
    <tr>
        <td>style_path</td>
        <td>Path&nbsp;to&nbsp;the&nbsp;css&nbsp;code</td>
    </tr>
    <tr>
        <td>charset</td>
        <td>encoding&nbsp;of&nbsp;css&nbsp;code</td>
    </tr>
    <tr>
        <td>return</td>
        <td>self</td>
    </tr>
</table>

<dt><a name="MyPy8TML-import_style"><strong>import_style</strong></a>(self, style_path, encoding='UTF-8')</dt><p> Import style from css code </p>

<table>
    <tr>
        <td>style_path</td>
        <td>Path&nbsp;to&nbsp;the&nbsp;css&nbsp;code</td>
    </tr>
    <tr>
        <td>encoding</td>
        <td>encoding&nbsp;of&nbsp;css&nbsp;code</td>
    </tr>
    <tr>
        <td>return</td>
        <td>self</td>
    </tr>
</table>

#  Dunder methods

<dl><dt><a name="MyPy8TML-__add__"><strong>__add__</strong></a>(self, other: str)</dt><dd>Add&nbsp;a&nbsp;string&nbsp;into&nbsp;a&nbsp;html, like to append</dd></dl>

<p> Use case: </p>

````python
MyPy8TML + str
````

<dl><dt><a name="MyPy8TML-__call__"><strong>__call__</strong></a>(self, times: int = 1, inline: str = '-')</dt><dd><tt> Closes the last htm tag, using times to close more than 1 , if negative closes inline</tt></dd></dl>

<p> Breaking line: </p>

````python
html = MyPy8TML().p()
print(html.generate())
````
    Inline:
````python
html = MyPy8TML().p(-1)
print(html.generate())
````


<dt><a name="MyPy8TML-__getitem__"><strong>__getitem__</strong></a>(self, item: str)</dt><p> The way to put content between tags </p>

<table> 
    <tr>
        <th> Param </th>
        <th> Description </th>
    </tr>
    <tr>
        <td>item</td>
        <td>Any&nbsp;string&nbsp;or&nbsp;a&nbsp;tuple&nbsp;(str,&nbsp;'in'&nbsp;or&nbsp;'out')</td>
    </tr>
    <tr>
        <td>item[1]</td>
        <td> if == 'in' put the content inside a tag if == 'out' contents go out</td>
    </tr>

</table>

<p>Exemple:</p> 

````python
html = MyPy8TML().p['Hello world ! ']
print(html.generate())
````

<p>In:</p>

````python
html = MyPy8TML().p['class="hello-world"', 'in']
print(html.generate())
````
<p>Out:</p>

````python
html = MyPy8TML().p['Hello world ! ', 'out']
print(html.generate())
````

# In properties

<em> Use these properties to write into tags </em>

<a name="MyPy8TML-in_content"><strong>in_content</strong></a>(self, content: str)<dd>
<p> Puts content inside a tag </p>


<table> 
    <tr>
        <th> content </th>
        <th> any&nbsp;kind&nbsp;of&nbsp;content&nbsp;ex:&nbsp;class='just-a-class' </th>
    </tr>
    <tr>
        <td>return</td>
        <td>self</td>
    </tr>
</table>

<dl><dt><a name="MyPy8TML-in_accesskey"><strong>in_accesskey</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_action"><strong>in_action</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_alt"><strong>in_alt</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_bgcolor"><strong>in_bgcolor</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_border"><strong>in_border</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_cellpadding"><strong>in_cellpadding</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_cellspacing"><strong>in_cellspacing</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_class"><strong>in_class</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_cols"><strong>in_cols</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_colspan"><strong>in_colspan</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_for"><strong>in_for</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_height"><strong>in_height</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_href"><strong>in_href</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_id"><strong>in_id</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_lang"><strong>in_lang</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_method"><strong>in_method</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_name"><strong>in_name</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_rows"><strong>in_rows</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_rowspan"><strong>in_rowspan</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_src"><strong>in_src</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_style"><strong>in_style</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_tabindex"><strong>in_tabindex</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_target"><strong>in_target</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_title"><strong>in_title</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_type"><strong>in_type</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_value"><strong>in_value</strong></a>(self, value: str)</dt></dl>

<dl><dt><a name="MyPy8TML-in_width"><strong>in_width</strong></a>(self, value: str)</dt></dl>

# Jinja in properties

<dl><dt><a name="MyPy8TML-jnj"><strong>jnj</strong></a>(self, expretion)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_add_bootstrap"><strong>jnj_add_bootstrap</strong></a>(self)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_block"><strong>jnj_block</strong></a>(self, name: str)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_comand"><strong>jnj_comand</strong></a>(self, comand)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_coment"><strong>jnj_coment</strong></a>(self, coment)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_elif"><strong>jnj_elif</strong></a>(self, expretion)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_else"><strong>jnj_else</strong></a>(self)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_endblock"><strong>jnj_endblock</strong></a>(self)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_endif"><strong>jnj_endif</strong></a>(self)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_expretion"><strong>jnj_expretion</strong></a>(self, expretion)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_extends_temp"><strong>jnj_extends_temp</strong></a>(self, template: str)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_if"><strong>jnj_if</strong></a>(self, expretion)</dt></dl>

<dl><dt><a name="MyPy8TML-jnj_include_temp"><strong>jnj_include_temp</strong></a>(self, template: str)</dt></dl>

<dl><dt><a name="MyPy8TML-sdnl"><strong>sdnl</strong></a> = <a href="#MyPy8TML-simple_down">simple_down</a>(self, times: int = 1)</dt></dl>


<br>


# Html tags 

<em> All html tags below are properties and return the SELF object. </em>

<dl><dt><strong>a</strong></dt>
</dl>
<dl><dt><strong>abbr</strong></dt>
</dl>
<dl><dt><strong>area</strong></dt>
</dl>
<dl><dt><strong>audio</strong></dt>
</dl>
<dl><dt><strong>b</strong></dt>
</dl>
<dl><dt><strong>body</strong></dt>
</dl>
<dl><dt><strong>br</strong></dt>
</dl>
<dl><dt><strong>button</strong></dt>
</dl>
<dl><dt><strong>canvas</strong></dt>
</dl>
<dl><dt><strong>caption</strong></dt>
</dl>
<dl><dt><strong>cite</strong></dt>
</dl>
<dl><dt><strong>code</strong></dt>
</dl>
<dl><dt><strong>col</strong></dt>
</dl>
<dl><dt><strong>colgroup</strong></dt>
</dl>
<dl><dt><strong>data</strong></dt>
</dl>
<dl><dt><strong>datalist</strong></dt>
</dl>
<dl><dt><strong>dfn</strong></dt>
</dl>
<dl><dt><strong>div</strong></dt>
</dl>
<dl><dt><strong>doctype</strong></dt>
</dl>
<dl><dt><strong>em</strong></dt>
</dl>
<dl><dt><strong>embed</strong></dt>
</dl>
<dl><dt><strong>fieldset</strong></dt>
</dl>
<dl><dt><strong>footer</strong></dt>
</dl>
<dl><dt><strong>form</strong></dt>
</dl>
<dl><dt><strong>h1</strong></dt>
</dl>
<dl><dt><strong>h2</strong></dt>
</dl>
<dl><dt><strong>h3</strong></dt>
</dl>
<dl><dt><strong>h4</strong></dt>
</dl>
<dl><dt><strong>h5</strong></dt>
</dl>
<dl><dt><strong>h6</strong></dt>
</dl>
<dl><dt><strong>head</strong></dt>
</dl>
<dl><dt><strong>header</strong></dt>
</dl>
<dl><dt><strong>html</strong></dt>
</dl>
<dl><dt><strong>i</strong></dt>
</dl>
<dl><dt><strong>iframe</strong></dt>
</dl>
<dl><dt><strong>img</strong></dt>
</dl>
<dl><dt><strong>input</strong></dt>
</dl>
<dl><dt><strong>kbd</strong></dt>
</dl>
<dl><dt><strong>label</strong></dt>
</dl>
<dl><dt><strong>legend</strong></dt>
</dl>
<dl><dt><strong>li</strong></dt>
</dl>
<dl><dt><strong>link</strong></dt>
</dl>
<dl><dt><strong>map</strong></dt>
</dl>
<dl><dt><strong>mark</strong></dt>
</dl>
<dl><dt><strong>meta</strong></dt>
</dl>
<dl><dt><strong>meter</strong></dt>
</dl>
<dl><dt><strong>nav</strong></dt>
</dl>
<dl><dt><strong>noscript</strong></dt>
</dl>
<dl><dt><strong>object</strong></dt>
</dl>
<dl><dt><strong>optgroup</strong></dt>
</dl>
<dl><dt><strong>option</strong></dt>
</dl>
<dl><dt><strong>output</strong></dt>
</dl>
<dl><dt><strong>p</strong></dt>
</dl>
<dl><dt><strong>pre</strong></dt>
</dl>
<dl><dt><strong>progress</strong></dt>
</dl>
<dl><dt><strong>q</strong></dt>
</dl>
<dl><dt><strong>s</strong></dt>
</dl>
<dl><dt><strong>samp</strong></dt>
</dl>
<dl><dt><strong>script</strong></dt>
</dl>
<dl><dt><strong>section</strong></dt>
</dl>
<dl><dt><strong>select</strong></dt>
</dl>
<dl><dt><strong>slot</strong></dt>
</dl>
<dl><dt><strong>small</strong></dt>
</dl>
<dl><dt><strong>source</strong></dt>
</dl>
<dl><dt><strong>span</strong></dt>
</dl>
<dl><dt><strong>strong</strong></dt>
</dl>
<dl><dt><strong>style</strong></dt>
</dl>
<dl><dt><strong>sub</strong></dt>
</dl>
<dl><dt><strong>sup</strong></dt>
</dl>
<dl><dt><strong>svg</strong></dt>
</dl>
<dl><dt><strong>table</strong></dt>
</dl>
<dl><dt><strong>tbody</strong></dt>
</dl>
<dl><dt><strong>td</strong></dt>
</dl>
<dl><dt><strong>template</strong></dt>
</dl>
<dl><dt><strong>textarea</strong></dt>
</dl>
<dl><dt><strong>tfoot</strong></dt>
</dl>
<dl><dt><strong>th</strong></dt>
</dl>
<dl><dt><strong>thead</strong></dt>
</dl>
<dl><dt><strong>time</strong></dt>
</dl>
<dl><dt><strong>title</strong></dt>
</dl>
<dl><dt><strong>tr</strong></dt>
</dl>
<dl><dt><strong>track</strong></dt>
</dl>
<dl><dt><strong>u</strong></dt>
</dl>
<dl><dt><strong>ul</strong></dt>
</dl>
<dl><dt><strong>var</strong></dt>
</dl>
<dl><dt><strong>video</strong></dt>
</dl>