from mypy_8tml import MyPy8TML
from random import Random

class Test:

    def test_downline_inline_close(self):
        html = MyPy8TML()
        html.p(-1).p(-1)
        assert html.generate() == '<p></p><p></p>'

    def test_downline_inline_with_randown_num_arg(self):
        num = round(Random().random() * 10)
        html = MyPy8TML()
        expected = ''
        for n in range(num):
            _ = html.p
            expected += '<p></p>'

        assert html(-num).generate() == expected


    def test_downline_no_agrs(self):
        html = MyPy8TML()
        html.p.downline().p.downline()
        assert html.generate() == '<p></p>\n' \
                                  '<p></p>\n'

    def test__call_with_no_close_no_agrs(self):
        html = MyPy8TML()
        html.img(-1).img(-1)
        assert html.generate() == '<img>\n' \
                                  '<img>\n'

    def test__call__no_agrs(self):
        html = MyPy8TML()
        html.p().p()
        assert html.generate() == '<p></p>\n' \
                                  '<p></p>\n'

    def test__call__inline_close(self):
        html = MyPy8TML()
        html.p(-1).p(-1)
        assert html.generate() == '<p></p><p></p>'

    def test_init_html(self):
        html = MyPy8TML()
        html.init_html(
            title='test',
            lang='en'
        )
        expected =f'<!DOCTYPE html>\n' \
                  f'<html lang="en" >\n' \
                  f'<head><meta charset="UTF-8" >\n' \
                  f'<title>test</title>\n' \
                  f'</head>\n' \
                  f'<body></body>'

        assert html.generate() == expected

    def test_if_init_html_puts_code_on_boody(self):
        html = MyPy8TML()
        html.init_html(
            title='test',
            lang='en'
        ).p['code']()

        expected = f'<!DOCTYPE html>\n' \
                   f'<html lang="en" >\n' \
                   f'<head><meta charset="UTF-8" >\n' \
                   f'<title>test</title>\n' \
                   f'</head>\n' \
                   f'<body><p>code</p>\n' \
                   f'</body>'

        assert html.generate() == expected

    def test_p(self):
        html = MyPy8TML()
        p = html.p.generate()
        assert p == '<p></p>'

    def test_h1(self):
        html = MyPy8TML()
        h1 = html.h1.generate()
        assert h1 == "<h1></h1>"

    def test_h2(self):
        html = MyPy8TML()
        h2 = html.h2.generate()
        assert h2 == "<h2></h2>"

    def test_h3(self):
        html = MyPy8TML()
        h3 = html.h3.generate()
        assert h3 == "<h3></h3>"

    def test_h4(self):
        html = MyPy8TML()
        h4 = html.h4.generate()
        assert h4 == "<h4></h4>"

    def test_h5(self):
        html = MyPy8TML()
        h5 = html.h5.generate()
        assert h5 == "<h5></h5>"

    def test_h6(self):
        html = MyPy8TML()
        h6 = html.h6.generate()
        assert h6 == "<h6></h6>"

    def test_a(self):
        html = MyPy8TML()
        a = html.a.generate()
        assert a == "<a></a>"

    def test_strong(self):
        html = MyPy8TML()
        strong = html.strong.generate()
        assert strong == "<strong></strong>"

    def test_em(self):
        html = MyPy8TML()
        em = html.em.generate()
        assert em == "<em></em>"

    def test_small(self):
        html = MyPy8TML()
        small = html.small.generate()
        assert small == "<small></small>"

    def test_s(self):
        html = MyPy8TML()
        s = html.s.generate()
        assert s == "<s></s>"

    def test_q(self):
        html = MyPy8TML()
        q = html.q.generate()
        assert q == "<q></q>"

    def test_cite(self):
        html = MyPy8TML()
        cite = html.cite.generate()
        assert cite == "<cite></cite>"

    def test_dfn(self):
        html = MyPy8TML()
        dfn = html.dfn.generate()
        assert dfn == "<dfn></dfn>"

    def test_abbr(self):
        html = MyPy8TML()
        abbr = html.abbr.generate()
        assert abbr == "<abbr></abbr>"

    def test_data(self):
        html = MyPy8TML()
        data = html.data.generate()
        assert data == "<data></data>"

    def test_time(self):
        html = MyPy8TML()
        time = html.time.generate()
        assert time == "<time></time>"

    def test_code(self):
        html = MyPy8TML()
        code = html.code.generate()
        assert code == "<code></code>"

    def test_var(self):
        html = MyPy8TML()
        var = html.var.generate()
        assert var == "<var></var>"

    def test_samp(self):
        html = MyPy8TML()
        samp = html.samp.generate()
        assert samp == "<samp></samp>"

    def test_kbd(self):
        html = MyPy8TML()
        kbd = html.kbd.generate()
        assert kbd == "<kbd></kbd>"

    def test_sup(self):
        html = MyPy8TML()
        sup = html.sup.generate()
        assert sup == "<sup></sup>"

    def test_sub(self):
        html = MyPy8TML()
        sub = html.sub.generate()
        assert sub == "<sub></sub>"

    def test_i(self):
        html = MyPy8TML()
        i = html.i.generate()
        assert i == "<i></i>"

    def test_b(self):
        html = MyPy8TML()
        b = html.b.generate()
        assert b == "<b></b>"

    def test_u(self):
        html = MyPy8TML()
        u = html.u.generate()
        assert u == "<u></u>"

    def test_mark(self):
        html = MyPy8TML()
        mark = html.mark.generate()
        assert mark == "<mark></mark>"

    def test_img(self):
        html = MyPy8TML()
        img = html.img.generate()
        assert img == "<img>"

    def test_video(self):
        html = MyPy8TML()
        video = html.video.generate()
        assert video == "<video></video>"

    def test_audio(self):
        html = MyPy8TML()
        audio = html.audio.generate()
        assert audio == "<audio></audio>"

    def test_source(self):
        html = MyPy8TML()
        source = html.source.generate()
        assert source == "<source>"

    def test_track(self):
        html = MyPy8TML()
        track = html.track.generate()
        assert track == "<track>"

    def test_map(self):
        html = MyPy8TML()
        map = html.map.generate()
        assert map == "<map></map>"

    def test_area(self):
        html = MyPy8TML()
        area = html.area.generate()
        assert area == "<area>"

    def test_object(self):
        html = MyPy8TML()
        object = html.object.generate()
        assert object == "<object></object>"

    def test_embed(self):
        html = MyPy8TML()
        embed = html.embed.generate()
        assert embed == "<embed>"

    def test_iframe(self):
        html = MyPy8TML()
        iframe = html.iframe.generate()
        assert iframe == "<iframe></iframe>"

    def test_canvas(self):
        html = MyPy8TML()
        canvas = html.canvas.generate()
        assert canvas == "<canvas></canvas>"

    def test_svg(self):
        html = MyPy8TML()
        svg = html.svg.generate()
        assert svg == "<svg></svg>"

    def test_table(self):
        html = MyPy8TML()
        table = html.table.generate()
        assert table == "<table></table>"

    def test_thead(self):
        html = MyPy8TML()
        thead = html.thead.generate()
        assert thead == "<thead></thead>"

    def test_tbody(self):
        html = MyPy8TML()
        tbody = html.tbody.generate()
        assert tbody == "<tbody></tbody>"

    def test_tfoot(self):
        html = MyPy8TML()
        tfoot = html.tfoot.generate()
        assert tfoot == "<tfoot></tfoot>"

    def test_tr(self):
        html = MyPy8TML()
        tr = html.tr.generate()
        assert tr == "<tr></tr>"

    def test_th(self):
        html = MyPy8TML()
        th = html.th.generate()
        assert th == "<th></th>"

    def test_td(self):
        html = MyPy8TML()
        td = html.td.generate()
        assert td == "<td></td>"

    def test_col(self):
        html = MyPy8TML()
        col = html.col.generate()
        assert col == "<col>"

    def test_colgroup(self):
        html = MyPy8TML()
        colgroup = html.colgroup.generate()
        assert colgroup == "<colgroup></colgroup>"

    def test_caption(self):
        html = MyPy8TML()
        caption = html.caption.generate()
        assert caption == "<caption></caption>"

    def test_form(self):
        html = MyPy8TML()
        form = html.form.generate()
        assert form == "<form></form>"

    def test_input(self):
        html = MyPy8TML()
        input = html.input.generate()
        assert input == "<input>"

    def test_button(self):
        html = MyPy8TML()
        button = html.button.generate()
        assert button == "<button></button>"

    def test_select(self):
        html = MyPy8TML()
        select = html.select.generate()
        assert select == "<select></select>"

    def test_datalist(self):
        html = MyPy8TML()
        datalist = html.datalist.generate()
        assert datalist == "<datalist></datalist>"

    def test_optgroup(self):
        html = MyPy8TML()
        optgroup = html.optgroup.generate()
        assert optgroup == "<optgroup></optgroup>"

    def test_option(self):
        html = MyPy8TML()
        option = html.option.generate()
        assert option == "<option></option>"

    def test_textarea(self):
        html = MyPy8TML()
        textarea = html.textarea.generate()
        assert textarea == "<textarea></textarea>"

    def test_label(self):
        html = MyPy8TML()
        label = html.label.generate()
        assert label == "<label></label>"

    def test_fieldset(self):
        html = MyPy8TML()
        fieldset = html.fieldset.generate()
        assert fieldset == "<fieldset></fieldset>"

    def test_legend(self):
        html = MyPy8TML()
        legend = html.legend.generate()
        assert legend == "<legend></legend>"

    def test_output(self):
        html = MyPy8TML()
        output = html.output.generate()
        assert output == "<output></output>"

    def test_progress(self):
        html = MyPy8TML()
        progress = html.progress.generate()
        assert progress == "<progress></progress>"

    def test_meter(self):
        html = MyPy8TML()
        meter = html.meter.generate()
        assert meter == "<meter></meter>"

    def test_head(self):
        html = MyPy8TML()
        head = html.head.generate()
        assert head == "<head></head>"

    def test_title(self):
        html = MyPy8TML()
        title = html.title.generate()
        assert title == "<title></title>"

    def test_meta(self):
        html = MyPy8TML()
        meta = html.meta.generate()
        assert meta == "<meta>"

    def test_style(self):
        html = MyPy8TML()
        style = html.style.generate()
        assert style == "<style></style>"

    def test_link(self):
        html = MyPy8TML()
        link = html.link.generate()
        assert link == "<link>"

    def test_script(self):
        html = MyPy8TML()
        script = html.script.generate()
        assert script == "<script></script>"

    def test_noscript(self):
        html = MyPy8TML()
        noscript = html.noscript.generate()
        assert noscript == "<noscript></noscript>"

    def test_template(self):
        html = MyPy8TML()
        template = html.template.generate()
        assert template == "<template></template>"

    def test_slot(self):
        html = MyPy8TML()
        slot = html.slot.generate()
        assert slot == "<slot></slot>"

    def test_body(self):
        html = MyPy8TML()
        body = html.body.generate()
        assert body == "<body></body>"




