print("これはsampleのモジュールです")

LOCATION = "日本"


def greet(name):
    honorific_title = "さん"
    # print(locals())
    print(F"こんにちは {LOCATION}　の {name} {honorific_title}")


def main():
    in_main_variable = 'hoge'

    def sub():
        print(in_main_variable)



