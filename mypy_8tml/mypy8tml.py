class MyPy8TML:
    def __init__(self):
        self._html = ''
        self._close = []
        self._final_atribut = None

    def generete(self) -> str:
        """ This method generetes the html final code. """
        return self._html + ''.join( self._close )

    def content(self, content: str):
        """ Add content to main html code """
        self._html += content
        return self

    def append(self, other):
        """
        :param other:           Another MyPy8TML object
        :type  other:           MyPy8TML
        :return:
        """
        self + other.generete()
        return self

    def __add__(self, other: str):
        self._html += other
        return self

    def _verify_html(self) -> None:
        if len( self._html ) <= 0:
            raise ValueError( 'There is no tags to put content inside.' )

    def _get_final_atribut(self):
        if len( self._close ) > 0:
            return self._final_atribut == self._close[-1].replace( '/', '' )
        return False

    def in_content(self, content: str):
        """
        Puts a content inside a tag
        :param content:  any kind of content ex: class='just-a-class'
        :return: self
        """
        self._verify_html()
        self._html = self._html[:-1]
        self._html += f' {content} >'
        return self

    def __getitem__(self, item: str or tuple[str, str]):
        """
        get item used in this case to add content inside or out of a tag
        :param item:            Any string or a tuple (str, 'in' or 'out')
        :argument item[1]:      if == 'in' put the content inside a tag if == 'out' contents go out
        """
        self._verify_html()
        if type( item ) == tuple:
            content, kind = item
            if kind == 'in':
                return self.in_content( content )
            elif kind == 'out':
                return self.content( content )
            else:
                raise ValueError( f'kind {kind} doesent exist!' )
        else:
            return self.content( item )

    def downline(self, times: int = 1):
        """
        This method allows to close a tag
        :param times:               Number of tags that you want to close
        :return:                    self
        """
        self._verify_html()
        for time in range( times ):
            content = self._close.pop( -1 )
            self._html += f'{content}\n'
        return self

    def simple_down(self, times: int = 1):
        """
        This method allows to just jump for next line
        :param times:           Number of tags that you want to go down in a code
        :return: self
        """
        for time in range( times ):
            self._html += f'\n'
        return self

    def _tag(self, tag, is_open: bool = True):
        """
        A generic method to a simple tag
        :param tag:         name of tag exemple <body>
        :type tag:          str
        :param is_open:     if the tag needs to be closed
        :type is_open:      bool
        :return: self
        """
        clean_tag = tag.replace( '<', '' ).replace( '>', '' )
        self._html += tag
        self._final_atribut = tag
        if is_open:
            self._close.append( f'</{clean_tag}>' )

    def __call__(self, times: int = 1):
        if self._get_final_atribut():
            self.dnl( times )
            return self
        else:
            self.sdnl( times )
            return self

    # Tags HTML

    @property
    def header(self):
        self._tag( "<header>", is_open=True )
        return self

    @property
    def div(self):
        self._tag( "<div>", is_open=True )
        return self

    @property
    def h1(self):
        self._tag( "<h1>", is_open=True )
        return self

    @property
    def h2(self):
        self._tag( "<h2>", is_open=True )
        return self

    @property
    def h3(self):
        self._tag( "<h3>", is_open=True )
        return self

    @property
    def h4(self):
        self._tag( "<h4>", is_open=True )
        return self

    @property
    def h5(self):
        self._tag( "<h5>", is_open=True )
        return self

    @property
    def h6(self):
        self._tag( "<h6>", is_open=True )
        return self

    @property
    def p(self):
        self._tag( "<p>", is_open=True )
        return self

    @property
    def a(self):
        self._tag( "<a>", is_open=True )
        return self

    @property
    def strong(self):
        self._tag( "<strong>", is_open=True )
        return self

    @property
    def em(self):
        self._tag( "<em>", is_open=True )
        return self

    @property
    def small(self):
        self._tag( "<small>", is_open=True )
        return self

    @property
    def s(self):
        self._tag( "<s>", is_open=True )
        return self

    @property
    def q(self):
        self._tag( "<q>", is_open=True )
        return self

    @property
    def cite(self):
        self._tag( "<cite>", is_open=True )
        return self

    @property
    def dfn(self):
        self._tag( "<dfn>", is_open=True )
        return self

    @property
    def abbr(self):
        self._tag( "<abbr>", is_open=True )
        return self

    @property
    def data(self):
        self._tag( "<data4scripts>", is_open=True )
        return self

    @property
    def time(self):
        self._tag( "<time>", is_open=True )
        return self

    @property
    def code(self):
        self._tag( "<code>", is_open=True )
        return self

    @property
    def var(self):
        self._tag( "<var>", is_open=True )
        return self

    @property
    def samp(self):
        self._tag( "<samp>", is_open=True )
        return self

    @property
    def kbd(self):
        self._tag( "<kbd>", is_open=True )
        return self

    @property
    def sup(self):
        self._tag( "<sup>", is_open=True )
        return self

    @property
    def sub(self):
        self._tag( "<sub>", is_open=True )
        return self

    @property
    def i(self):
        self._tag( "<i>", is_open=True )
        return self

    @property
    def b(self):
        self._tag( "<b>", is_open=True )
        return self

    @property
    def u(self):
        self._tag( "<u>", is_open=True )
        return self

    @property
    def mark(self):
        self._tag( "<mark>", is_open=True )
        return self

    @property
    def img(self):
        self._tag( "<img>", is_open=False )
        return self

    @property
    def video(self):
        self._tag( "<video>", is_open=True )
        return self

    @property
    def audio(self):
        self._tag( "<audio>", is_open=True )
        return self

    @property
    def source(self):
        self._tag( "<source>", is_open=False )
        return self

    @property
    def track(self):
        self._tag( "<track>", is_open=False )
        return self

    @property
    def map(self):
        self._tag( "<map>", is_open=True )
        return self

    @property
    def area(self):
        self._tag( "<area>", is_open=False )
        return self

    @property
    def object(self):
        self._tag( "<object>", is_open=True )
        return self

    @property
    def embed(self):
        self._tag( "<embed>", is_open=False )
        return self

    @property
    def iframe(self):
        self._tag( "<iframe>", is_open=True )
        return self

    @property
    def canvas(self):
        self._tag( "<canvas>", is_open=True )
        return self

    @property
    def svg(self):
        self._tag( "<svg>", is_open=True )
        return self

    @property
    def table(self):
        self._tag( "<table>", is_open=True )
        return self

    @property
    def thead(self):
        self._tag( "<thead>", is_open=True )
        return self

    @property
    def tbody(self):
        self._tag( "<tbody>", is_open=True )
        return self

    @property
    def tfoot(self):
        self._tag( "<tfoot>", is_open=True )
        return self

    @property
    def tr(self):
        self._tag( "<tr>", is_open=True )
        return self

    @property
    def th(self):
        self._tag( "<th>", is_open=True )
        return self

    @property
    def td(self):
        self._tag( "<td>", is_open=True )
        return self

    @property
    def ul(self):
        self._tag( "<ul>", is_open=True )
        return self

    @property
    def col(self):
        self._tag( "<col>", is_open=False )
        return self

    @property
    def colgroup(self):
        self._tag( "<colgroup>", is_open=True )
        return self

    @property
    def caption(self):
        self._tag( "<caption>", is_open=True )
        return self

    @property
    def form(self):
        self._tag( "<form>", is_open=True )
        return self

    @property
    def input(self):
        self._tag( "<input>", is_open=False )
        return self

    @property
    def button(self):
        self._tag( "<button>", is_open=True )
        return self

    @property
    def select(self):
        self._tag( "<select>", is_open=True )
        return self

    @property
    def datalist(self):
        self._tag( "<datalist>", is_open=True )
        return self

    @property
    def optgroup(self):
        self._tag( "<optgroup>", is_open=True )
        return self

    @property
    def option(self):
        self._tag( "<option>", is_open=True )
        return self

    @property
    def textarea(self):
        self._tag( "<textarea>", is_open=True )
        return self

    @property
    def label(self):
        self._tag( "<label>", is_open=True )
        return self

    @property
    def fieldset(self):
        self._tag( "<fieldset>", is_open=True )
        return self

    @property
    def legend(self):
        self._tag( "<legend>", is_open=True )
        return self

    @property
    def output(self):
        self._tag( "<output>", is_open=True )
        return self

    @property
    def progress(self):
        self._tag( "<progress>", is_open=True )
        return self

    @property
    def meter(self):
        self._tag( "<meter>", is_open=True )
        return self

    @property
    def head(self):
        self._tag( "<head>", is_open=True )
        return self

    @property
    def title(self):
        self._tag( "<title>", is_open=True )
        return self

    @property
    def meta(self):
        self._tag( "<meta>", is_open=False )
        return self

    @property
    def style(self):
        self._tag( "<style>", is_open=True )
        return self

    @property
    def link(self):
        self._tag( "<link>", is_open=False )
        return self

    @property
    def script(self):
        self._tag( "<script>", is_open=True )
        return self

    @property
    def noscript(self):
        self._tag( "<noscript>", is_open=True )
        return self

    @property
    def template(self):
        self._tag( "<template>", is_open=True )
        return self

    @property
    def slot(self):
        self._tag( "<slot>", is_open=True )
        return self

    @property
    def doctype(self):
        self._tag( "<!DOCTYPE html>", is_open=False )
        return self

    @property
    def html(self):
        self._tag( "<html>", is_open=False )
        return self

    @property
    def body(self):
        self._tag( "<body>", is_open=True )
        return self

    # Atributos html

    def in_alt(self, value: str):
        self.in_content( f'alt: "{value}"' )
        return self

    def in_method(self, value: str):
        self.in_content( f'method: "{value}"' )
        return self

    def in_type(self, value: str):
        self.in_content( f'type: "{value}"' )
        return self

    def in_title(self, value: str):
        self.in_content( f'title: "{value}"' )
        return self

    def in_bgcolor(self, value: str):
        self.in_content( f'bgcolor: "{value}"' )
        return self

    def in_src(self, value: str):
        self.in_content( f'src: "{value}"' )
        return self

    def in_width(self, value: str):
        self.in_content( f'width: "{value}"' )
        return self

    def in_colspan(self, value: str):
        self.in_content( f'colspan: "{value}"' )
        return self

    def in_cols(self, value: str):
        self.in_content( f'cols: "{value}"' )
        return self

    def in_rows(self, value: str):
        self.in_content( f'rows: "{value}"' )
        return self

    def in_accesskey(self, value: str):
        self.in_content( f'accesskey: "{value}"' )
        return self

    def in_border(self, value: str):
        self.in_content( f'border: "{value}"' )
        return self

    def in_class(self, value: str):
        self.in_content( f'class: "{value}"' )
        return self

    def in_action(self, value: str):
        self.in_content( f'action: "{value}"' )
        return self

    def in_rowspan(self, value: str):
        self.in_content( f'rowspan: "{value}"' )
        return self

    def in_value(self, value: str):
        self.in_content( f'value: "{value}"' )
        return self

    def in_lang(self, value: str):
        self.in_content( f'lang: "{value}"' )
        return self

    def in_style(self, value: str):
        self.in_content( f'style: "{value}"' )
        return self

    def in_cellpadding(self, value: str):
        self.in_content( f'cellpadding: "{value}"' )
        return self

    def in_height(self, value: str):
        self.in_content( f'height: "{value}"' )
        return self

    def in_cellspacing(self, value: str):
        self.in_content( f'cellspacing: "{value}"' )
        return self

    def in_target(self, value: str):
        self.in_content( f'target: "{value}"' )
        return self

    def in_id(self, value: str):
        self.in_content( f'id: "{value}"' )
        return self

    def in_tabindex(self, value: str):
        self.in_content( f'tabindex: "{value}"' )
        return self

    def in_name(self, value: str):
        self.in_content( f'name: "{value}"' )
        return self

    def in_href(self, value: str):
        self.in_content( f'href: "{value}"' )
        return self

    def init_html(self, title, lang: str, charset="UTF-8"):
        html = self \
            .doctype() \
            .html[f'lang="{lang}"', 'in']() \
            .head \
            .meta[f'charset="{charset}"', 'in']() \
            .title[title]( 2 ) \
            .body
        return self

    def import_style(self, style_path, encoding='UTF-8'):
        with open(style_path, 'rt', encoding=encoding) as file:
            css: str = file.read()
            _ = self.style[css]()


    dnl = downline
    sdnl = simple_down
