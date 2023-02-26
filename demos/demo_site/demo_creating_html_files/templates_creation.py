from mypy_8tml import MyPy8TML


def generate_templates():
    # Index
    with MyPy8TML(file_name='index.html', path='templates/') as index:
        index.init_html('My Form', 'en')\
            .div.in_class('container')\
                .form.in_class('form').in_action('/submit').in_method('POST')\
                    .h1['My Form']()\
                    .p['Name:'](-1).input.in_type('text').in_name('name')()\
                    .p['Email:'](-1).input.in_type('email').in_name('email')()\
                    .p['Message:'](-1).textarea.in_name('message')()\
                    .button.in_type('submit')['Submit']()

    # About page
    with MyPy8TML(file_name='about.html', path='templates/') as about:
        about.init_html('About Us', 'en')\
            .div.in_class('container')\
                .h1['About Us']()\
                .p['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec '\
                   'nibh id dolor blandit mollis non ut mauris.']()

    # Contact page
    with MyPy8TML(file_name='contact.html', path='templates/') as contact:
        contact.init_html('Contact Us', 'en')\
            .div.in_class('container')\
                .h1['Contact Us']()\
                .form.in_class('form').in_action('/submit').in_method('POST')\
                    .p['Name:'](-1).input.in_type('text').in_name('name')()\
                    .p['Email:'](-1).input.in_type('email').in_name('email')()\
                    .p['Message:'](-1).textarea.in_name('message')()\
                    .button.in_type('submit')['Submit']()