def test_var_args(f_arg, *argv):
    print(f"first normal arg: {f_arg}")
    for arg in argv:
        print(f"another arg through *argv: {arg}")

test_var_args('sujay', 'python', 'test')


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

greet_me(name='sujay')
