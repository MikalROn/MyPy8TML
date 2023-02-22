from mypy_8tml import MyPy8TML



with MyPy8TML(file_name='index', path='templates') as index:
    code = \
        index\
            .div\
                .button.in_class('bnt')['Click me!']()\
                .b.p[' Este botão e incrivel! '](2)\
                .input.in_type('password')