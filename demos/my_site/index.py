from mypy_8tml import MyPy8TML



with MyPy8TML() as index:
    code = \
        index\
            .div\
                .button.in_class('bnt')['Click me!']()\
                .b.p[' Este botão e incrivel! '](2)\
                .input.in_type('password')