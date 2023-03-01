# Methods

<br>

##  **Dunder methods**

<dl><dt><a name="MyPy8TML-__add__"><strong>__add__</strong></a>(self, other: str)</dt><dd><tt>Add&nbsp;a&nbsp;string&nbsp;into&nbsp;a&nbsp;html, like to append</tt></dd></dl>

<P> Use case: 

````python
MyPy8TML + str
````

<dl><dt><a name="MyPy8TML-__call__"><strong>__call__</strong></a>(self, times: int = 1, inline: str = '-')</dt><dd><tt> Closes the last htm tag, using times to close more than 1 , if negative closes inline</tt></dd></dl>

<br>

Breaking line:
````python
html = MyPy8TML().p()
print(html.generate())
````
Inline:
````python
html = MyPy8TML().p(-1)
print(html.generate())
````

<br>


<dl><dt><a name="MyPy8TML-__getitem__"><strong>__getitem__</strong></a>(self, item: str)</dt><dd><tt>The way to put content between tags<br>

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

Exemple:
````python
html = MyPy8TML().p['Hello world ! ']
print(html.generate())
````
In:
````python
html = MyPy8TML().p['class="hello-world"', 'in']
print(html.generate())
````
Out:
````python
html = MyPy8TML().p['Hello world ! ', 'out']
print(html.generate())
````

<br>



<dl><dt><a name="MyPy8TML-content"><strong>content</strong></a>(self, content: str)</dt><dd><tt>Add&nbsp;content&nbsp;to&nbsp;main&nbsp;html&nbsp;code</tt></dd></dl>

<dl><dt><a name="MyPy8TML-downline"><strong>downline</strong></a>(self, times: int = 1)</dt><dd><tt>This&nbsp;method&nbsp;allows&nbsp;to&nbsp;close&nbsp;a&nbsp;tag<br>
:param&nbsp;times:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;tags&nbsp;that&nbsp;you&nbsp;want&nbsp;to&nbsp;go&nbsp;down&nbsp;in&nbsp;a&nbsp;code<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;negative&nbsp;close&nbsp;tag&nbsp;inline<br>
:return:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self</tt></dd></dl>

<dl><dt><a name="MyPy8TML-generate"><strong>generate</strong></a>(self) -&gt; str</dt><dd><tt>This&nbsp;method&nbsp;generetes&nbsp;the&nbsp;html&nbsp;final&nbsp;code.</tt></dd></dl>

<dl><dt><a name="MyPy8TML-import_html"><strong>import_html</strong></a>(self, style_path, charset='UTF-8') -&gt; None</dt><dd><tt>Import&nbsp;html&nbsp;code&nbsp;from&nbsp;file&nbsp;code<br>
:param&nbsp;style_path:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Path&nbsp;to&nbsp;the&nbsp;css&nbsp;code<br>
:param&nbsp;charset:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encoding&nbsp;of&nbsp;css&nbsp;code<br>
:return:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;self</tt></dd></dl>

<dl><dt><a name="MyPy8TML-import_style"><strong>import_style</strong></a>(self, style_path, encoding='UTF-8')</dt><dd><tt>Import&nbsp;style&nbsp;from&nbsp;css&nbsp;code<br>
:param&nbsp;style_path:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Path&nbsp;to&nbsp;the&nbsp;css&nbsp;code<br>
:param&nbsp;encoding:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encoding&nbsp;of&nbsp;css&nbsp;code<br>
:return:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;self</tt></dd></dl>

## In properties

<em> All of this features 
   </em>

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

<dl><dt><a name="MyPy8TML-in_content"><strong>in_content</strong></a>(self, content: str)</dt><dd><tt>Puts&nbsp;content&nbsp;inside&nbsp;a&nbsp;tag<br>
:param&nbsp;content:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any&nbsp;kind&nbsp;of&nbsp;content&nbsp;ex:&nbsp;class='just-a-class'<br>
:return:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self</tt></dd></dl>

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

<dl><dt><a name="MyPy8TML-init_html"><strong>init_html</strong></a>(self, title, lang: str, charset='UTF-8', inhead: str = '')</dt><dd><tt>Generates&nbsp;the&nbsp;stat&nbsp;of&nbsp;a&nbsp;html&nbsp;code&nbsp;until&nbsp;the&nbsp;bod<br>
&nbsp;<br>
&lt;!DOCTYPE&nbsp;html&gt;<br>
&lt;html&nbsp;lang=":param&nbsp;lang:"}&gt;<br>
&lt;head&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;:param&nbsp;inhead:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;meta&nbsp;charset=":param&nbsp;charset:"&gt;<br>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;title&gt;:param&nbsp;title:&lt;/title&gt;<br>
&lt;/head&gt;<br>
&lt;body&gt;&nbsp;{UNTIL&nbsp;HERE}<br>
&nbsp;<br>
:param&nbsp;title:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;title&nbsp;of&nbsp;your&nbsp;html&nbsp;page<br>
:param&nbsp;lang:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lang&nbsp;of&nbsp;html<br>
:param&nbsp;charset:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;charset&nbsp;of&nbsp;html<br>
:param&nbsp;inhead:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;puts&nbsp;content&nbsp;un&nbsp;head<br>
:return:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self</tt></dd></dl>

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

<dl><dt><a name="MyPy8TML-set_filename"><strong>set_filename</strong></a>(self, name: str)</dt><dd><tt>Set&nbsp;the&nbsp;name&nbsp;of&nbsp;output&nbsp;file</tt></dd></dl>

<dl><dt><a name="MyPy8TML-simple_down"><strong>simple_down</strong></a>(self, times: int = 1)</dt><dd><tt>This&nbsp;method&nbsp;allows&nbsp;to&nbsp;just&nbsp;jump&nbsp;for&nbsp;next&nbsp;line<br>
:param&nbsp;times:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;tags&nbsp;that&nbsp;you&nbsp;want&nbsp;to&nbsp;go&nbsp;down&nbsp;in&nbsp;a&nbsp;code<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;negative&nbsp;close&nbsp;tag&nbsp;inline<br>
:return:&nbsp;self</tt></dd></dl>

<dl><dt><a name="MyPy8TML-to_html"><strong>to_html</strong></a>(self, name: str, path: str = '') -&gt; None</dt><dd><tt>Export&nbsp;to&nbsp;Html<br>
:param&nbsp;name:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;of&nbsp;html&nbsp;code&nbsp;with&nbsp;sufix<br>
:param&nbsp;path:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path&nbsp;to&nbsp;put&nbsp;code&nbsp;with&nbsp;slash&nbsp;bar<br>
:return:&nbsp;None</tt></dd></dl>


<br>


<br>

<h1> Html tags </h1>

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